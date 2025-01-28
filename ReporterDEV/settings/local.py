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
        'NAME': 'reporterdev',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}