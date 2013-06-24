
import os
from .tests import TEST_ROOT

#import pdb; pdb.set_trace()

#print os.environ
#print os.getenv('DATABASE_PROVIDER')
DATABASE_PROVIDER = os.getenv('DATABASE_PROVIDER', 'sqlite3')

if DATABASE_PROVIDER == 'sqlite3':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.getenv('DATABASE_NAME', TEST_ROOT / "db" / "mitx.db"),
        },
    }
elif DATABASE_PROVIDER == 'mysql':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': os.getenv('DATABASE_HOST', '127.0.0.1'),
            'NAME': os.getenv('DATABASE_NAME', 'wwc'),
            'PASSWORD': os.getenv('DATABASE_PASSWORD', ''),
            'PORT': os.getenv('DATABASE_PORT', '3306'),
            'USER': os.getenv('DATABASE_USER', 'root'),
        }
    }
