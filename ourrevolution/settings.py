"""
Django settings for ourrevolution project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import dj_database_url
import mimetypes
import os
import re


mimetypes.add_type('image/svg+xml', 'svg')


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', None)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get('DEBUG', '1')))

ALLOWED_HOSTS = ['our-revolution-cms.herokuapp.com', 'localhost', 'ourrevolution.com', 'www.ourrevolution.com', 'beta.ourrevolution.com']

ADMINS = [('Jon Culver', 'jon@ourrevolution.com'), ('Chris Mabry', 'chris@ourrevolution.com')]

MANAGERS = ADMINS


# Application definition

INSTALLED_APPS = [

    #Django gulp
    'django_gulp',

    'anymail',

    # Django core
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'debug_toolbar',

    # Wagtail
    'wagtail.wagtailforms',
    'wagtail.wagtailredirects',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsites',
    'wagtail.wagtailusers',
    'wagtail.wagtailsnippets',
    'wagtail.wagtaildocs',
    'wagtail.wagtailimages',
    'wagtail.wagtailsearch',
    'wagtail.wagtailadmin',
    'wagtail.wagtailcore',
    'modelcluster',
    'taggit',

    # S3
    'storages',

    # OR.
    'endorsements',
    'pages',
    'social_redirects'
]

SERVER_EMAIL = "bugtroll@ourrevolution.com"

INTERNAL_IPS = ['24.18.176.26', '24.158.161.75']

MIDDLEWARE = [

    # debug
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    # Django core
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Wagtail
    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',

    # OR
    'social_redirects.middleware.RedirectFallbackMiddleware'    

]

ROOT_URLCONF = 'ourrevolution.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ourrevolution.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {'default': dj_database_url.config()}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, '.static')

WAGTAIL_SITE_NAME = 'Our Revolution'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/' if os.environ.get('env', 'development') != 'production' else 'https://s3.amazonaws.com/our-revolution-dot-com/'


if os.environ.get('env', 'development') == 'production':

    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', None)
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', None)
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', None)
    AWS_QUERYSTRING_AUTH = False

    AWS_AUTO_CREATE_BUCKET = True
    # AWS_DEFAULT_ACL


TEST_RUNNER = 'pages.tests.NoDbTestRunner'



MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY', None)
MAILGUN_SENDER_DOMAIN = os.environ.get('MAILGUN_SENDER_DOMAIN', None)


ANYMAIL = {
    'MAILGUN_API_KEY': MAILGUN_API_KEY,
    'MAILGUN_SENDER_DOMAIN': MAILGUN_SENDER_DOMAIN
}

EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'anymail.backends.mailgun.MailgunBackend')

IGNORABLE_404_URLS = [
        re.compile(r'^favicon\.ico'),
        re.compile(r'^/img/candidates/.*')
    ]
