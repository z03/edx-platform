import sys
import os
import logging
from path import path
from importlib import import_module
from mock import patch
from nose.tools import assert_equals, with_setup
from pprint import pprint
from contextlib import contextmanager


IGNORE_KEY_VALUES = {
    'MAKO_MODULE_DIR',
    'WIKI_CAN_CHANGE_PERMISSIONS',
    'WIKI_CAN_ASSIGN'
}

@contextmanager
def patch_environ(patch):
    old_values = {}
    for key, value in patch.items():
        old_values[key] = os.getenv(key)
        os.environ[key] = value
    yield
    for key, value in old_values.items():
        if value is None:
            del os.environ[key]
        else:
            os.environ[key] = value

def settings_keys(settings):
    return {key for key in dir(settings) if key.upper() == key}


def reload_modules():
    for module_name, module in sys.modules.items():
        if not module:
            continue

        if module_name.startswith('lms') or module_name.startswith('cms'):
            reload(module)


def assert_same_keys(left, right):
    assert_equals(settings_keys(left), settings_keys(right))

def assert_key_equal(key, left, right):
    left_val = getattr(left, key)
    right_val = getattr(right, key)

    if left_val != right_val:
        pprint(left_val)
        pprint(right_val)

    assert_equals(getattr(left, key), getattr(right, key))

def import_settings_with_env(path, environment):
    with patch_environ({'DJANGO_SETTINGS_MODULE': path}):
        with patch_environ(environment):
            reload_modules()
            return import_module(path)

def test_settings():
    for system in ('lms', 'cms'):
    #for system in ('lms',):
        env_root = path(system) / 'envs'
        for env in env_root.files():
        #for env in (env_root / 'devplus.py',):
            if not env.endswith('.py'):
                continue

            env = env.basename().replace('.py', '')
            old_settings = "{}.envs.{}".format(system, env)

            env_file = path(system) / (env + '.env')
            if env_file.exists():
                with open(env_file) as env_contents:
                    env_settings = dict(line.strip().split('=') for line in env_contents)
            else:
                env_settings = {}

            new_settings = "{}.settings".format(system)

            try:
                old_settings_module = import_settings_with_env(old_settings, {})
            except:
                # Make failed settings imports appear as failed tests
                yield import_settings_with_env, old_settings, {}
                continue

            try:
                new_settings_module = import_settings_with_env(new_settings, env_settings)
            except:
                # Make failed settings imports appear as failed tests
                yield import_settings_with_env, new_settings, env_settings
                continue


            yield assert_same_keys, old_settings_module, new_settings_module

            try:
                old_keys = settings_keys(old_settings_module)
            except:
                logging.exception('Failure while loading keys for %s', old_settings)
                old_keys = set()

            try:
                new_keys = settings_keys(new_settings_module)
            except:
                logging.exception('Failure while loading keys for %s under %s', new_settings, env_settings)
                new_keys = set()

            for key in old_keys & new_keys:
                if key in IGNORE_KEY_VALUES:
                    continue

                yield assert_key_equal, key, old_settings_module, new_settings_module
