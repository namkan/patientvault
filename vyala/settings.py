"""
Django settings for vyala project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import dj_database_url
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4$nv$-ly(^h1b+qbua4m)6t$2s6a&b!=g^b01z9&p!d#q_0(u1'

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
    'whitenoise.runserver_nostatic',
    'registration',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vyala.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'vyala.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
	    'NAME' : 'patientvault',
	    'USER' : 'root',
	    'PASSWORD' : 'jishnu12',
	    'HOST' : 'localhost',
	    'port' : '5432',
    }
     
}

FILE_UPLOAD_HANDLERS = (
    "testapp.dropbox_upload_handler.DropboxFileUploadHandler",
)
DROPBOX_APP_KEY = "ves55dpyfxanqg0"
DROPBOX_APP_SECRET_KEY = "tygyq0xdtky4ici"
DROPBOX_APP_ACCESS_TOKEN = ""
DROPBOX_APP_ACCESS_TOKEN_SECRET = ""

# Optional values below

# The folder where you want the files uploaded.
# Example: /Public or /
DROPBOX_FILE_UPLOAD_FOLDER = ""
# The value below may be either 'app_folder' or 'dropbox'
DROPBOX_ACCESS_TYPE = ""


db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_HOST_USER = 'naman.kansal@vyalatech.com'
EMAIL_HOST_PASSWORD = '9756089119'
EMAIL_PORT = 587
#EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_USE_SSL = True
# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

SESSION_COOKIE_AGE = 1000

# AUTHENTICATION_BACKENDS = (
#         'django.contrib.auth.backends.ModelBackend',
#     )

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

if DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
    STATICFILES_DIRS = (
        os.path.join(PROJECT_DIR, 'static').replace('\\','/'),
    )
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
STATICFILES_DIRS = (
        os.path.join(PROJECT_DIR, 'static').replace('\\','/'),
    )