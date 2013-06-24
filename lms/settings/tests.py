import os
from path import path

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
SOUTH_TESTS_MIGRATE = False
TEST_ROOT = path('test_root')

if os.environ.get('TESTING'):

    #http://slacy.com/blog/2012/04/make-your-tests-faster-in-django-1-4/
    PASSWORD_HASHERS = (
        # 'django.contrib.auth.hashers.PBKDF2PasswordHasher',
        # 'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
        # 'django.contrib.auth.hashers.BCryptPasswordHasher',
        'django.contrib.auth.hashers.SHA1PasswordHasher',
        'django.contrib.auth.hashers.MD5PasswordHasher',
        # 'django.contrib.auth.hashers.CryptPasswordHasher',
    )

    CELERY_ALWAYS_EAGER = True
    CELERY_RESULT_BACKEND = 'cache'
    BROKER_TRANSPORT = 'memory'

    JASMINE_REPORT_DIR = os.environ.get('JASMINE_REPORT_DIR', 'reports/lms/jasmine')

