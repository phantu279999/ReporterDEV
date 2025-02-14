# python manage.py runserver --settings=config.settings.local

from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS += [
	'debug_toolbar',
]

# Debug Toolbar settings
INTERNAL_IPS = [
	"127.0.0.1",
]

# REST_FRAMEWORK = {
# 	'DEFAULT_PERMISSION_CLASSES': {
# 		'rest_framework.permissions.IsAdminUser',
# 	}
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': os.getenv('MYSQL_DATABASE', 'reporterdev'),
        # 'USER': os.getenv('MYSQL_USER', 'root'),
        # 'PASSWORD': os.getenv('MYSQL_PASSWORD', '1234'),
        # 'HOST': 'db',
        'NAME': 'reporterdev',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}


API_URL = 'http://localhost:8000/api/v1/'
