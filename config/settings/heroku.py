import os
from .base import *


# DEBUG
# ------------------------------------------------------------------------------
DEBUG = True
ALLOWED_HOSTS = ['*']
ADMINS = ['nashruddin.amin@gmail.com']

# SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# ------------------------------------------------------------------------------
SECRET_KEY = os.getenv('SECRET_KEY')

# DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
# ------------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
    }
}

# HEROKU CONFIGURATION
# ------------------------------------------------------------------------------
import django_heroku
django_heroku.settings(locals())
