import os
from .base import *


SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {}
}

import django_heroku
django_heroku.settings(locals())
