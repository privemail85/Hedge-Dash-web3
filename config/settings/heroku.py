import os

import django_heroku
from .base import *


SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = True
ALLOWED_HOSTS = ['*']
ADMINS = ['nashruddin.amin@gmail.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
    }
}

EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
ANYMAIL = {
    'MAILGUN_API_KEY': os.getenv('MAILGUN_API_KEY'),
    'MAILGUN_SENDER_DOMAIN': os.getenv('MAILGUN_SENDER_DOMAIN'),
}
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', 'noreply@example.com')

django_heroku.settings(locals())
