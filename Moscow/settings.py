"""
Django settings for Moscow project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rarcan!uux&6c)462-dc&bcju%9stz3ft#g(!)q!9tor6k4w8h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*'
]


# Application definition

INSTALLED_APPS = [
#    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
    'common',
    'dashboard',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Moscow.urls'


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

WSGI_APPLICATION = 'Moscow.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'NAME': 'moscow',
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '123456',
        'OPTIONS': {'init_command': 'SET default_storage_engine=InnoDB'},
        'CHARSET': 'utf8',
        'COLLATION': 'utf8_general_ci',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'


USE_I18N = True

USE_L10N = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]


ENTRY_CONFIG = {
    'london': {
        'WECHAT_APP_ID': 'wx69b1df2db40d33f5',
        'WECHAT_APP_SECRET': 'c7003b84d2a85598ce4e051d2f76706e',
        'WXPAY_MCH_ID': '1495032292',
        'WXPAY_API_KEY': 'aWNhdGUgQXV0aG9yXR5Q0wwYDVQQDEwR'
    },
    'paris': {
        'WECHAT_APP_ID': 'wxd4eae843e18ff7da',
        'WECHAT_APP_SECRET': '510861ca183551e3a7fcbdc87573c00f',
        'WXPAY_MCH_ID': '1495032292',
        'WXPAY_API_KEY': 'aWNhdGUgQXV0aG9yXR5Q0wwYDVQQDEwR'
    },
    'milan': {
        'WECHAT_APP_ID': 'wxe1d7d4370a4d0976',
        'WECHAT_APP_SECRET': '4d3dce0a7eb45c42b5b1f292ab7c6a76',
        'WXPAY_MCH_ID': '1495032292',
        'WXPAY_API_KEY': 'aWNhdGUgQXV0aG9yXR5Q0wwYDVQQDEwR'
    }
}
