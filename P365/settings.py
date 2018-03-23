"""
Django settings for P365 project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0m!x2+t&33wa7()n6&!@k5w*f8guh(b+*!!xa_3s7*&y2snn8v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.gis',
    'leaflet',
    'bootstrap3',
    'tagulous',

    'calendar_year',
    'gpx',
    'tag',
    'map',
    'profile',
    'story',
    'table',
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

ROOT_URLCONF = 'P365.urls'

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

WSGI_APPLICATION = 'P365.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

SPATIALITE_LIBRARY_PATH = 'mod_spatialite'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join('static'),)

# Auth settings
LOGIN_URL = '/login/'

# Map settings
# https://django-leaflet.readthedocs.io

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (30, 0),
    'DEFAULT_ZOOM': 2,
    'RESET_VIEW': False,
    'PLUGINS': {
        'elevation': {
            'css': os.path.join(STATIC_URL, 'css/leaflet.elevation.css'),
            'js': [os.path.join(STATIC_URL, 'js/leaflet.elevation.min.js'),
                   os.path.join(STATIC_URL, 'js/d3.min.js')],
            'auto-include': False
        }
    },
    'TILES': [
        ('OpenStreetMap', 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            'maxZoom': 19, 'attribution': '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
        }),
        ('OpenStreetMap B&W', 'http://{s}.tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png', {
            'maxZoom': 18, 'attribution': '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
        }),
        ('OpenTopoMap', 'https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
            'maxZoom': 17,
            'attribution': 'Map data: &copy;'
                           ' <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>,'
                           ' <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy;'
                           ' <a href="https://opentopomap.org">OpenTopoMap</a>'
                           ' (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)',
        }),
        ('Toner', 'https://stamen-tiles-{s}.a.ssl.fastly.net/toner/{z}/{x}/{y}.{ext}', {
            'attribution': 'Map tiles by <a href="http://stamen.com">Stamen Design</a>,'
                           ' <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy;'
                           ' <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
            'subdomains': 'abcd',
            'minZoom': 0,
            'maxZoom': 20,
            'ext': 'png'
        }),
        ('TonerLite', 'https://stamen-tiles-{s}.a.ssl.fastly.net/toner-lite/{z}/{x}/{y}.{ext}', {
            'attribution': 'Map tiles by <a href="http://stamen.com">Stamen Design</a>,'
                           ' <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy;'
                           ' <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
            'subdomains': 'abcd',
            'minZoom': 0,
            'maxZoom': 20,
            'ext': 'png'
        }),
        ('WorldStreetMap',
         'https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}', {
             'attribution': 'Tiles &copy; Esri &mdash; 2012'
         }),
        ('WorldTopoMap',
         'https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}', {
             'attribution': 'Tiles &copy; Esri'
         }),
        ('WorldImagery',
         'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
             'attribution': 'Tiles &copy; Esri'
         }),
    ],
}

MAX_LENGTH = {
    'name': 30,
    'description': 250,
    'title': 50,
    'text': 5000,
    'tag': 30,
}
