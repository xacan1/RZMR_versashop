"""
Django settings for versa project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
# python manage.py makemessages -l ru
# python manage.py compilemessages -l ru

from django.utils.translation import gettext_lazy as _
from pathlib import Path
from versa import config

try:
    from versa.local_settings import *
except ImportError:
    from versa.prod_settings import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.SECRET_KEY
ADMIN_PANEL_URL = config.ADMIN_PANEL_URL

# Для онлайн магазина признак того, что можно превышать остатки на складах при заказе
EXCESS_STOCK_OF_GOODS = config.EXCESS_STOCK_OF_GOODS

COMPANY_NAME = config.COMPANY_NAME
COMPANY_NAME_SHORT = config.COMPANY_NAME_SHORT
COMPANY_EMAIL = config.COMPANY_EMAIL
COMPANY_ADDRESS = config.COMPANY_ADDRESS
EMAIL_USER = config.EMAIL_USER

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_recaptcha',
]

VERSA_APPS = [
    'rzmr.apps.RzmrConfig',
    'shop.apps.ShopConfig',
    'personal_account.apps.PersonalAccountConfig',
    'main.apps.MainConfig',
    'blog.apps.BlogConfig',
    'api.apps.ApiConfig',
    'constructor.apps.ConstructorConfig',
    'rest_framework',
    'rest_framework.authtoken',
]

# if DEBUG:
#     DEBUG_APPS = ['debug_toolbar',]
#     INSTALLED_APPS += DEBUG_APPS

INSTALLED_APPS += VERSA_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# if DEBUG:
#     VERSA_MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware',]
#     MIDDLEWARE += VERSA_MIDDLEWARE
#     INTERNAL_IPS = ['127.0.0.1',]

ROOT_URLCONF = 'versa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'versa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'OPTIONS': {
            'timeout': 60,
            # 'check_same_thread': False, 
            # 'uri': True,
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru'

LANGUAGES = (
    ('ru', _('Russian')),
    ('kk', _('Kazakh')),
    ('en', _('English')),
)

LOCALE_PATHS = (
    BASE_DIR / 'locale',
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'main.CustomUser'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
}

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_FILE_PATH = BASE_DIR / 'send_emails'
DEFAULT_FROM_EMAIL = f'{ALLOWED_HOSTS[0]} <{EMAIL_USER}>'
EMAIL_HOST = config.EMAIL_SMTP
EMAIL_HOST_USER = EMAIL_USER
EMAIL_HOST_PASSWORD = config.EMAIL_PASSWORD
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False

MANAGERS = config.ADMINS

APPEND_SLASH = True

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'django.db.backends': {
#             'level': 'DEBUG',
#             'handlers': ['console'],
#         }
#     },
# }

# SESSION_COOKIE_AGE = 24 * 60 * 60
# DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880
