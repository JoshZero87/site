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

"""Fastly and Varnish caching"""
CACHE_FRONTEND_ENABLED = bool(int(os.environ.get('CACHE_FRONTEND_ENABLED', 0)))

CSRF_COOKIE_SECURE = bool(int(os.environ.get('CSRF_COOKIE_SECURE', 0)))

"""Auto approve events created by Group Leaders"""
EVENT_AUTO_APPROVAL = bool(int(os.environ.get(
    'EVENT_AUTO_APPROVAL',
    0
)))

"""Local Groups Roles"""
LOCAL_GROUPS_ROLE_GROUP_ADMIN_ID = 2
LOCAL_GROUPS_ROLE_GROUP_LEADER_ID = 1

# Organizing Hub Urls
ORGANIZING_HUB_DASHBOARD_URL = '/organizing-hub/'
ORGANIZING_GUIDES_URL = '/docs/organizing-guides/'
ORGANIZING_DOCS_URL = '/docs/'

SESSION_COOKIE_SECURE = bool(int(os.environ.get('SESSION_COOKIE_SECURE', 0)))

BSD_CREATE_ACCOUNT_URL = os.environ.get(
    'BSD_CREATE_ACCOUNT_URL',
    'https://ourrevdev.cp.bsd.net/ctl/Constituent/Login'
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', None)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get('DEBUG', '1')))

DEFAULT_FROM_EMAIL = "info@ourrevolution.com"
ACCOUNT_ADAPTER = ("local_groups.adapter.AccountAdapter")
ACCOUNT_EMAIL_SUBJECT_PREFIX = ""

ALLOWED_HOSTS = '*'

ADMINS = [
    ('Our Revolution Tech Team', 'tech-team@ourrevolution.com'),
]

CANDIDATES_URL = '/candidates/'

MANAGERS = ADMINS

# Application definition
'''
When several applications provide different versions of the same resource
(template, static file, management command, translation), the application listed
first in INSTALLED_APPS has precedence.
'''
INSTALLED_APPS = [

    # OR apps
    'endorsements',
    'organizing_hub',
    'pages',
    'social_redirects',
    'transform',
    'local_groups',
    'nominations',
    'bsd',

    # Other apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

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
    "wagtail.contrib.table_block",
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

DATABASES = {'default': dj_database_url.config()}
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

# BSD login urls
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'bsd.backends.BSDAuthenticationBackend',
)
BSD_API_HOST = os.environ.get('BSD_API_HOST')
BSD_API_ID = os.environ.get('BSD_API_ID')
BSD_API_SECRET = os.environ.get('BSD_API_SECRET')
LOGIN_URL = 'groups-login'
LOGIN_REDIRECT_URL = ORGANIZING_HUB_DASHBOARD_URL

SHOP_NAV_ENABLED = bool(int(os.environ.get('SHOP_NAV_ENABLED', 0)))

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

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

WAGTAIL_SITE_NAME = 'Our Revolution'

"""
Set base url for wagtail email notifications
https://github.com/wagtail/wagtail/issues/826
"""
BASE_URL = os.environ.get('BASE_URL', 'http://localhost:8000')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = os.environ.get('MEDIA_URL', '/media/')

"""ID of 'Briefly list important local issues...' Question"""
NOMINATIONS_QUESTION_ISSUES_ID = 24

ADD_GROUP_URL = '/groups/new/'
ELECTORAL_COORDINATOR_EMAIL = str(os.environ.get(
    'ELECTORAL_COORDINATOR_EMAIL',
    'political@ourrevolution.com'
))
OR_ADDRESS_CITY = 'Washington'
OR_ADDRESS_STATE = 'DC'
OR_ADDRESS_STREET = 'PO Box 66208'
OR_ADDRESS_ZIP = '20035'
OR_LOGO_SECONDARY = 'https://our-revolution-dot-com.s3.amazonaws.com/images/our-revolution-logo-secondary-300x353.original.png'
OR_META_IMAGE_URL = '/static/dist/img/our-revolution-meta-image.png'
ORGANIZING_EMAIL = 'organizing@ourrevolution.com'
RESULTS_URL = '/results/'
RESULTS_2016_URL = '/election-2016/'
RESULTS_2017_URL = '/2017-elections-results/'
START_GROUP_URL = 'https://docs.google.com/document/d/1BWp6HCZ6tngr6SJHJB3H1uPTX2Hcv6cMUQondCrBkHg/edit'

DEFAULT_FILE_STORAGE = os.environ.get(
    'DEFAULT_FILE_STORAGE',
    'django.core.files.storage.FileSystemStorage'
)
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', None)
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', None)
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', None)
AWS_QUERYSTRING_AUTH = bool(int(os.environ.get('AWS_QUERYSTRING_AUTH', '1')))
AWS_AUTO_CREATE_BUCKET = bool(int(os.environ.get(
    'AWS_AUTO_CREATE_BUCKET',
    '0'
)))

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

if CACHE_FRONTEND_ENABLED and not DEBUG:

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
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
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
