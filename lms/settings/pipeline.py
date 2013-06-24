import os.path

from .paths import PROJECT_ROOT, COMMON_ROOT, DATA_DIR


############################### Pipeline #######################################

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

from rooted_paths import rooted_glob

courseware_js = (
    [
        'coffee/src/' + pth + '.js'
        for pth in ['courseware', 'histogram', 'navigation', 'time']
    ] +
    sorted(rooted_glob(PROJECT_ROOT / 'static', 'coffee/src/modules/**/*.js'))
)

# 'js/vendor/RequireJS.js' - Require JS wrapper.
# See https://edx-wiki.atlassian.net/wiki/display/LMS/Integration+of+Require+JS+into+the+system
main_vendor_js = [
  'js/vendor/RequireJS.js',
  'js/vendor/json2.js',
  'js/vendor/jquery.min.js',
  'js/vendor/jquery-ui.min.js',
  'js/vendor/jquery.cookie.js',
  'js/vendor/jquery.qtip.min.js',
  'js/vendor/swfobject/swfobject.js',
  'js/vendor/jquery.ba-bbq.min.js',
  'js/vendor/annotator.min.js',
  'js/vendor/annotator.store.min.js',
  'js/vendor/annotator.tags.min.js'
]

discussion_js = sorted(rooted_glob(PROJECT_ROOT / 'static', 'coffee/src/discussion/**/*.js'))
staff_grading_js = sorted(rooted_glob(PROJECT_ROOT / 'static', 'coffee/src/staff_grading/**/*.js'))
open_ended_js = sorted(rooted_glob(PROJECT_ROOT / 'static', 'coffee/src/open_ended/**/*.js'))
notes_js = sorted(rooted_glob(PROJECT_ROOT / 'static', 'coffee/src/notes/**/*.coffee'))

PIPELINE_CSS = {
    'application': {
        'source_filenames': ['sass/application.css'],
        'output_filename': 'css/lms-application.css',
    },
    'course': {
        'source_filenames': [
            'js/vendor/CodeMirror/codemirror.css',
            'css/vendor/jquery.treeview.css',
            'css/vendor/ui-lightness/jquery-ui-1.8.22.custom.css',
            'css/vendor/jquery.qtip.min.css',
            'css/vendor/annotator.min.css',
            'sass/course.css',
            'xmodule/modules.css',
        ],
        'output_filename': 'css/lms-course.css',
    },
    'ie-fixes': {
        'source_filenames': ['sass/ie.css'],
        'output_filename': 'css/lms-ie.css',
    },
}


# test_order: Determines the position of this chunk of javascript on
# the jasmine test page
PIPELINE_JS = {
    'application': {

        # Application will contain all paths not in courseware_only_js
        'source_filenames': sorted(
            set(rooted_glob(COMMON_ROOT / 'static', 'coffee/src/**/*.js') +
                rooted_glob(PROJECT_ROOT / 'static', 'coffee/src/**/*.js')) -
            set(courseware_js + discussion_js + staff_grading_js + open_ended_js + notes_js)
        ) + [
            'js/form.ext.js',
            'js/my_courses_dropdown.js',
            'js/toggle_login_modal.js',
            'js/sticky_filter.js',
            'js/query-params.js',
        ],
        'output_filename': 'js/lms-application.js',

        'test_order': 1,
    },
    'courseware': {
        'source_filenames': courseware_js,
        'output_filename': 'js/lms-courseware.js',
        'test_order': 2,
    },
    'main_vendor': {
        'source_filenames': main_vendor_js,
        'output_filename': 'js/lms-main_vendor.js',
        'test_order': 0,
    },
    'module-js': {
        'source_filenames': rooted_glob(COMMON_ROOT / 'static', 'xmodule/modules/js/*.js'),
        'output_filename': 'js/lms-modules.js',
        'test_order': 3,
    },
    'discussion': {
        'source_filenames': discussion_js,
        'output_filename': 'js/discussion.js',
        'test_order': 4,
    },
    'staff_grading': {
        'source_filenames': staff_grading_js,
        'output_filename': 'js/staff_grading.js',
        'test_order': 5,
    },
    'open_ended': {
        'source_filenames': open_ended_js,
        'output_filename': 'js/open_ended.js',
        'test_order': 6,
    },
    'notes': {
        'source_filenames': notes_js,
        'output_filename': 'js/notes.js',
        'test_order': 7
    },
}

PIPELINE_DISABLE_WRAPPER = True

# Compile all coffee files in course data directories if they are out of date.
# TODO: Remove this once we move data into Mongo. This is only temporary while
# course data directories are still in use.
if os.path.isdir(DATA_DIR):
    for course_dir in os.listdir(DATA_DIR):
        js_dir = DATA_DIR / course_dir / "js"
        if not os.path.isdir(js_dir):
            continue
        for filename in os.listdir(js_dir):
            if filename.endswith('coffee'):
                new_filename = os.path.splitext(filename)[0] + ".js"
                if os.path.exists(js_dir / new_filename):
                    coffee_timestamp = os.stat(js_dir / filename).st_mtime
                    js_timestamp = os.stat(js_dir / new_filename).st_mtime
                    if coffee_timestamp <= js_timestamp:
                        continue
                os.system("rm %s" % (js_dir / new_filename))
                os.system("coffee -c %s" % (js_dir / filename))


PIPELINE_CSS_COMPRESSOR = None
PIPELINE_JS_COMPRESSOR = None

STATICFILES_IGNORE_PATTERNS = (
    "sass/*",
    "coffee/*",
)

PIPELINE_YUI_BINARY = 'yui-compressor'

# Setting that will only affect the MITx version of django-pipeline until our changes are merged upstream
PIPELINE_COMPILE_INPLACE = True

if os.getenv('JASMINE_TESTING'):
    PIPELINE_JS['js-test-source'] = {
        'source_filenames': sum([
            pipeline_group['source_filenames']
            for group_name, pipeline_group
            in sorted(PIPELINE_JS.items(), key=lambda item: item[1].get('test_order', 1e100))
            if group_name != 'spec'
        ], []),
        'output_filename': 'js/lms-test-source.js'
    }

    PIPELINE_JS['spec'] = {
        'source_filenames': sorted(rooted_glob(PROJECT_ROOT / 'static/', 'coffee/spec/**/*.js')),
        'output_filename': 'js/lms-spec.js'
    }