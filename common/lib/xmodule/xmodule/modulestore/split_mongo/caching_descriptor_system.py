import sys
import logging
from xmodule.mako_module import MakoDescriptorSystem
from xmodule.x_module import XModuleDescriptor
from xmodule.modulestore.locator import BlockUsageLocator, LocalId
from xmodule.error_module import ErrorDescriptor
from xmodule.errortracker import exc_info_to_str
from xblock.runtime import DbModel
from ..exceptions import ItemNotFoundError
from .split_mongo_kvs import SplitMongoKVS
from xblock.fields import ScopeIds

log = logging.getLogger(__name__)


class CachingDescriptorSystem(MakoDescriptorSystem):
    """
    A system that has a cache of a course version's json that it will use to load modules
    from, with a backup of calling to the underlying modulestore for more data.

    Computes the settings (nee 'metadata') inheritance upon creation.
    """
    def __init__(self, modulestore, course_entry, default_class, module_data, lazy, **kwargs):
        """
        Computes the settings inheritance and sets up the cache.

        modulestore: the module store that can be used to retrieve additional
        modules

        module_data: a dict mapping Location -> json that was cached from the
            underlying modulestore
        """
        # TODO find all references to resources_fs and make handle None
        super(CachingDescriptorSystem, self).__init__(load_item=self._load_item, **kwargs)
        self.modulestore = modulestore
        self.course_entry = course_entry
        self.lazy = lazy
        self.module_data = module_data
        # TODO see if self.course_id is needed: is already in course_entry but could be > 1 value
        # Compute inheritance
        modulestore.inherit_settings(
            course_entry.get('blocks', {}),
            course_entry.get('blocks', {}).get(course_entry.get('root'))
        )
        self.default_class = default_class
        self.local_modules = {}

    def _load_item(self, usage_id, course_entry_override=None):
        # TODO ensure all callers of system.load_item pass just the id

        if isinstance(usage_id, BlockUsageLocator) and isinstance(usage_id.usage_id, LocalId):
            try:
                return self.local_modules[usage_id]
            except KeyError:
                raise ItemNotFoundError

        json_data = self.module_data.get(usage_id)
        if json_data is None:
            # deeper than initial descendant fetch or doesn't exist
            self.modulestore.cache_items(self, [usage_id], lazy=self.lazy)
            json_data = self.module_data.get(usage_id)
            if json_data is None:
                raise ItemNotFoundError

        class_ = XModuleDescriptor.load_class(
            json_data.get('category'),
            self.default_class
        )
        return self.xblock_from_json(class_, usage_id, json_data, course_entry_override)

    def xblock_from_json(self, class_, usage_id, json_data, course_entry_override=None):
        if course_entry_override is None:
            course_entry_override = self.course_entry
        # most likely a lazy loader or the id directly
        definition = json_data.get('definition', {})
        definition_id = self.modulestore.definition_locator(definition)

        # If no usage id is provided, generate an in-memory id
        if usage_id is None:
            usage_id = LocalId()

        block_locator = BlockUsageLocator(
            version_guid=course_entry_override['_id'],
            usage_id=usage_id,
            course_id=course_entry_override.get('course_id'),
            branch=course_entry_override.get('branch')
        )

        kvs = SplitMongoKVS(
            definition,
            json_data.get('fields', {}),
            json_data.get('_inherited_settings'),
        )
        field_data = DbModel(kvs)

        try:
            module = self.construct_xblock_from_class(
                class_,
                field_data,
                ScopeIds(None, json_data.get('category'), definition_id, block_locator)
            )
        except Exception:
            log.warning("Failed to load descriptor", exc_info=True)
            return ErrorDescriptor.from_json(
                json_data,
                self,
                BlockUsageLocator(
                    version_guid=course_entry_override['_id'],
                    usage_id=usage_id
                ),
                error_msg=exc_info_to_str(sys.exc_info())
            )

        edit_info = json_data.get('edit_info', {})
        module.edited_by = edit_info.get('edited_by')
        module.edited_on = edit_info.get('edited_on')
        module.previous_version = edit_info.get('previous_version')
        module.update_version = edit_info.get('update_version')
        module.definition_locator = self.modulestore.definition_locator(definition)
        # decache any pending field settings
        module.save()

        # If this is an in-memory block, store it in this system
        if isinstance(block_locator.usage_id, LocalId):
            self.local_modules[block_locator] = module

        return module
