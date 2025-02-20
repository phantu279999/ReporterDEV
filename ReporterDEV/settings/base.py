import os
import json
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured


BASE_DIR = Path(__file__).resolve().parent.parent.parent
SECRETS_FILE = BASE_DIR / 'secrets.json'


if not SECRETS_FILE.exists():
    raise ImproperlyConfigured("secrets.json file is missing!")

with open(SECRETS_FILE) as f:
    secrets = json.load(f)


def get_secret(setting, secrets=secrets):
    '''Get the secret variable or return explicit exception.'''
    try:
        return secrets[setting]
    except KeyError:
        raise ImproperlyConfigured(f"Set the {setting} environment variable.")


# Build paths inside the project like this: BASE_DIR / 'subdir'.
MEDIA_DIR = BASE_DIR / 'media'
STATIC_DIR = BASE_DIR / 'static'



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',

	# 3rd party
	'ckeditor',
	'rest_framework',
	'rest_framework.authtoken',
	'django_filters',
	'djoser',
	'drf_yasg',
	'django_celery_results',

	# app
	'core.apps.CoreConfig',
	'accounts.apps.AccountsConfig',
]

AUTH_USER_MODEL = 'accounts.CustomUser'

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	"debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'ReporterDEV.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [BASE_DIR / 'templates']
		,
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]

WSGI_APPLICATION = 'ReporterDEV.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': BASE_DIR / 'db.sqlite3',
	}
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
	{
		'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
	},
]

# AUTHENTICATION_BACKENDS = [
#     'accounts.auth.CustomUserBackend',
#     'django.contrib.auth.backends.ModelBackend',  # Fallback backend
# ]

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
	STATIC_DIR,
]

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

API_URL = '/api/v1/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
	"DEFAULT_AUTHENTICATION_CLASSES": [
		"rest_framework.authentication.BasicAuthentication",
		"rest_framework.authentication.SessionAuthentication",
		"rest_framework.authentication.TokenAuthentication",
		# "rest_framework_simplejwt.authentication.JWTAuthentication"
	],
	"DEFAULT_PERMISSION_CLASSES": [
		'rest_framework.permissions.IsAuthenticatedOrReadOnly'
	],
	'DEFAULT_THROTTLE_CLASSESS': [
		'rest_framework.throttling.AnonRateThrottle',
		'rest_framework.throttling.UserRateThrottle'
	],
	'DEFAULT_THROTTLE_RATES': {
		'anon': '500/day',
		'user': '2000/day',
	},
	"DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
	"PAGE_SIZE": 10,
	"DEFAULT_FILTER_BACKENDS": [
		"django_filters.rest_framework.DjangoFilterBackend",
		"rest_framework.filters.OrderingFilter"
	],
}

DJOSER = {
    'SERIALIZERS': {
        'user': 'core.api.serializers.CustomDjoserUserSerializer',
    }
}

CELERY_RESULT_BACKEND = "django-db"
CELERY_BROKER_URL = "redis://localhost:6379/0"