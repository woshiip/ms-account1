"""
Django settings for serviceB project.

Generated by 'django-admin startproject' using Django 1.8.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#t^5@&ze2$$wlle(&cqt*25szg$+0q)uv36qcp^$4(o$lve2uz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['104.197.239.117','127.0.0.1',]

# Application definition
REST_FRAMEWORK = {
    "DATE_INPUT_FORMATS": [("%Y-%m-%d"), ],
    'DATE_FORMAT': "%Y-%m-%d",
    'DATE_INPUT_FORMATS': ("%Y-%m-%d",),

    'DATETIME_FORMAT': "%Y-%m-%d %H:%M:%S",
    'DATETIME_INPUT_FORMATS': ("%Y-%m-%d %H:%M:%S",),

    'TIME_FORMAT': '%H:%M:%S',
    'TIME_INPUT_FORMATS': ('%H:%M:%S',),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        ),
    'DEFAULT_RENDERER_CLASSES': ['rest_framework.renderers.JSONRenderer', ],

    # 'rest_framework.renderers.BrowsableAPIRenderer',

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
        ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        ),
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
        'rest_framework.throttling.ScopedRateThrottle',
        ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '30/minute',
        'user': '100/minute',
        'suggest': '5/minute',
        'sms-code': '5/minute',
        'upload-image': '5/minute',
        'order': '3/minute',
        'cart': '5/minute',
        'tenPerMin': '10/minute',
        'fivePerMin': '5/minute',
        'threePerMin': '3/minute',
        'onePerMin': '1/minute',
        'twelvePerMin': '12/minute',
        },

    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    # GET https://api.example.org/accounts/?limit=20&offset=0
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 50,
    }

if DEBUG:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].append('rest_framework.renderers.BrowsableAPIRenderer')

INSTALLED_APPS = (
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    "account"
    )

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    )

ROOT_URLCONF = 'serviceB.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'serviceB.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'accounts',
        'USER': 'root',         # 数据库用户名
        'PASSWORD': '123456',     # 密码
        'HOST': '10.108.6.19',    # 主机
        'PORT': '3306',         # 数据库使用的端口
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
