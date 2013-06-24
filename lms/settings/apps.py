import os

################################### APPS ######################################
INSTALLED_APPS = (
    # Standard ones that are always installed...
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'djcelery',
    'south',

    # Monitor the status of services
    'service_status',

    # For asset pipelining
    'mitxmako',
    'pipeline',
    'staticfiles',
    'static_replace',

    # Our courseware
    'circuit',
    'courseware',
    'perfstats',
    'student',
    'static_template_view',
    'staticbook',
    'track',
    'util',
    'certificates',
    'instructor',
    'instructor_task',
    'open_ended_grading',
    'psychometrics',
    'licenses',
    'course_groups',

    #For the wiki
    'wiki',  # The new django-wiki from benjaoming
    'django_notify',
    'course_wiki',  # Our customizations
    'mptt',
    'sekizai',
    #'wiki.plugins.attachments',
    'wiki.plugins.links',
    'wiki.plugins.notifications',
    'course_wiki.plugins.markdownedx',

    # foldit integration
    'foldit',

    # For testing
    'django.contrib.admin',  # only used in DEBUG mode
    'debug',

    # Discussion forums
    'django_comment_client',
    'django_comment_common',
    'notes',
)

if os.getenv('TESTING'):
    INSTALLED_APPS += ('django_nose', 'external_auth', 'django_openid_auth')

if os.getenv('JASMINE_TESTING'):
    INSTALLED_APPS += ('django_jasmine', 'settings_context_processor')
