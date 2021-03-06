# -*- coding: utf-8 -*-
"""
Django settings for first_project project.

Generated by 'django-admin startproject' using Django 1.11.7.

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
SECRET_KEY = '(it=2)^#t8zx5mo@@)^1r2_bunq-h8@pp^x1ne5(p13x=qd1pi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False  #debug true es para desarrollo
#This is my server, change this hosts
ALLOWED_HOSTS = ['www.zuccheroapp.tk','35.229.43.71']
EMAIL_HOST = 'smtp.gmail.com'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
EMAIL_HOST_USER ='sender@ejemplo.com'  #Que sea Gmail
EMAIL_HOST_PASSWORD = 'passwordrealdesender'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

"""
Para usar gmail hay que desbloquear captcha 
https://accounts.google.com/displayunlockedcaptcha
"""


# Application definition
INSTALLED_APPS = [
    #apps django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #apps terceros
    'crispy_forms',
    'registration',
    #mis apps
    'boletin',
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

ROOT_URLCONF = 'first_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'first_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'


#esto solo cuando se está en desarrollo(para simular el proceso de produccion)
#esto es tener los statics files en un servidor y django en otro

STATICFILES_DIRS = [os.path.join(BASE_DIR,"static_pro","static"),]  #base dir es la raiz del proyecto

#nombre del directorio donde vive base_Dire
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),"static_env","static_root")
#archivos de terceros(clientes, eg: obtenido por formularios)
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR),"static_env","media_root")

ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
SITE_ID =1
LOGIN_REDIRECT_URL = '/'
CRYSPY_TEMPLATE_PACK = 'uni_form'

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True

