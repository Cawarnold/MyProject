"""
Django settings for hellodjango project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Default
#> # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#> import os
#> BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#> STATIC_URL = '/static/'

import os

#### STATIC ASSETS AND FILE SERVING ####
# Default
#> # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#> import os
#> BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#> STATIC_URL = '/static/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ob^%q9z#d*jry&_rtj2#(r2z92m)_^pji28!yjtl&7igqe$c^@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []



# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'hellodjango.urls'

WSGI_APPLICATION = 'hellodjango.wsgi.application'



#### DATABASES ####
# Default
#> # https://docs.djangoproject.com/en/1.7/ref/settings/#databases
#> 
#> DATABASES = {
#>     'default': {
#>         'ENGINE': 'django.db.backends.sqlite3',
#>         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#>     }
#> }

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()
DATABASES['default']['ENGINE'] = 'django_postgrespool'

# Database connection pooling is a great way to improve the performance of your Django application.
# Databases in the Heroku Postgres starter tier have a maximum connection limit of 20. 
# In that case your pool_size and max_overflow, when combined, should not exceed 20.
## https://warehouse.python.org/project/django-postgrespool/

DATABASE_POOL_ARGS = {
    'max_overflow': 10,
    'pool_size': 5,
    'recycle': 300
}


#### INTERNATIONALIZATION ####
# Languages, Time Zones
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



#### OTHER SETTINGS ####

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']



