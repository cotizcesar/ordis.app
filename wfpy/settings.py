"""
Django settings for wfpy project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xu8ru(2tip&@t41o4z3839srs3x_%ovjj-tkv$9(k31)=3i*mi'

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
    # Django: For numbers, text and anoher things.
    'django.contrib.humanize',
    # easy_thumbnails: Images handle and thumbnails generator.
    'easy_thumbnails',
    # WFPY: Core (Index, Pages, etc)
    'core',
    # WFPY: User Profiles app.
    'userprofile',
    # WFPY: Market app.
    'market',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'wfpy.urls'
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
                # Core: Search Input in header, loads all items in database.
                'core.context_processors.external_data',
                # Core: User counter
                #'core.context_processors.user_count',
            ],
        },
    },
]
WSGI_APPLICATION = 'wfpy.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/2.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# easy-thumbnails: Extension when a image its transparent.
THUMBNAIL_TRANSPARENCY_EXTENSION = 'png'

# easy-thumbnails: Every size for all images.
THUMBNAIL_ALIASES = {
    '': {
        'avatar': {'size': (200, 200), 'crop': 'smart', 'upscale' : True},
        'avatar_aside': {'size': (40, 40), 'crop': 'smart', 'upscale' : True},
        'avatar_header': {'size': (30, 30), 'crop': 'smart', 'upscale' : True},
        'item': {'size': (200, 200), 'crop': 'smart', 'upscale' : True},
        'order': {'size': (74, 74), 'crop': 'smart', 'upscale' : True},
    },
}

# easy_thumbnails: Renaming the image uploads.
THUMBNAIL_NAMER = 'easy_thumbnails.namers.hashed'

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())