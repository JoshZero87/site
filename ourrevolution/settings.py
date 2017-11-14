"""
Django settings for ourrevolution project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

from collections import OrderedDict
import dj_database_url, mimetypes, os, re


mimetypes.add_type('image/svg+xml', 'svg')


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', None)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get('DEBUG', '1')))

ALLOWED_HOSTS = '*'

ADMINS = [
    # ('Chris Mabry', 'chris@ourrevolution.com'),
    ('Eric Broder', 'eric@ourrevolution.com')
]

MANAGERS = ADMINS


# Application definition
'''
When several applications provide different versions of the same resource
(template, static file, management command, translation), the application listed
first in INSTALLED_APPS has precedence.
'''
INSTALLED_APPS = [

    # OR
    'endorsements',
    'pages',
    'social_redirects',
    'local_groups',
    'nominations',
    'bsd',

    #Django gulp
    'django_gulp',

    'anymail',
    'django.contrib.humanize',

    # Django core
    'django.contrib.gis',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 'debug_toolbar',

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

    #
    'wagtail.contrib.wagtailfrontendcache',
    'wagtail.contrib.wagtailroutablepage',

    # Group Goodies
    'phonenumber_field',
    'multiselectfield',
    'django_countries',
    'recurrence',
    'address',
    'bootstrap3',
    'crispy_forms',
    'ckeditor',
    'easy_pdf',

    # S3
    'storages'
]

CRISPY_TEMPLATE_PACK = 'bootstrap3'
CRISPY_FAIL_SILENTLY = not DEBUG

PHONENUMBER_DB_FORMAT = "E164"
PHONENUMBER_DEFAULT_REGION = "US"

SERVER_EMAIL = "bugtroll@ourrevolution.com"

INTERNAL_IPS = ['24.18.176.26', '24.158.161.75', '127.0.0.1']

MIDDLEWARE = [

    # debug
    'django.middleware.gzip.GZipMiddleware',
    # 'django.middleware.common.BrokenLinkEmailsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',

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

BSD_API_HOST    = os.environ.get('BSD_API_HOST')
BSD_API_ID      = os.environ.get('BSD_API_ID')
BSD_API_SECRET  = os.environ.get('BSD_API_SECRET')

DATABASES = {
    'default': dj_database_url.config(),
}
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

# DATABASE_ROUTERS = ['bsd.routers.BSDRouter']

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'bsd.backends.BSDAuthenticationBackend',
)

# BSD login urls
# TODO: replace temp urls with real urls when pages are ready
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/login/'

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

# Set base url for wagtail email notifications https://github.com/wagtail/wagtail/issues/826
BASE_URL = 'http://localhost:8000' if os.environ.get('env', 'development') != 'production' else 'https://ourrevolution.com'

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

GOOGLE_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY', None)

ANYMAIL = {
    'MAILGUN_API_KEY': MAILGUN_API_KEY,
    'MAILGUN_SENDER_DOMAIN': MAILGUN_SENDER_DOMAIN
}

EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'anymail.backends.mailgun.MailgunBackend')

IGNORABLE_404_URLS = [
        re.compile(r'^/favicon\.ico'),
        re.compile(r'^/img/candidates/.*')
    ]


WAGTAILEMBEDS_EMBED_FINDER = 'ourrevolution.embeds.oembed_monkeypatched'

if not DEBUG:

    WAGTAILFRONTENDCACHE = OrderedDict((

        ('elb-varnish', {
            'BACKEND': 'pages.frontendcache.backends.ElasticLoadBalancedVarnishBackend',
            'LOAD_BALANCER_NAME': 'ourrevcms',
            'PROFILE_NAME': 'ourrevcms',
            'REGION': 'us-west-2',
            'PORT': 8080,
            'HOST_NAMES': ['ourrevolution.com', 'www.ourrevolution.com', 'ourrevcms-17735885.us-west-2.elb.amazonaws.com'],
        }),

        ('fastly', {
            'BACKEND': 'pages.frontendcache.backends.FastlyBackend',
            'HOSTS': ['http://ourrevolution.com', 'https://ourrevolution.com', 'http://www.ourrevolution.com', 'https://www.ourrevolution.com'],
            'API_KEY': os.environ.get('FASTLY_API_KEY', None)
        })

    ))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'console': {
            'level': 'NOTSET',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'django-debug.log',
        },
        'SysLog': {
    		'level': 'NOTSET',
    		'class': 'logging.handlers.SysLogHandler',
    		'formatter': 'simple',
    		'address': ('logs6.papertrailapp.com', 17716)
    	},
    },
    'formatters': {
    	'simple': {
    		'format': '%(asctime)s ourrevolution.com: %(message)s',
            'datefmt': '%Y-%m-%dT%H:%M:%S',
    	},
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'NOTSET',
        },
        'django.request': {
            'handlers': ['mail_admins', 'console','SysLog'],
            'level': 'ERROR',
            'propagate': True,
        },
        'nominations': {
            'handlers': ['console','SysLog'],
            'level': 'DEBUG',
            'propagate': True,
        }
    },
}
