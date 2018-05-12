import os
from .base import *


SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {}
}

EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
ANYMAIL = {
    'MAILGUN_API_KEY': os.getenv('MAILGUN_API_KEY'),
    'MAILGUN_SENDER_DOMAIN': os.getenv('MAILGUN_SENDER_DOMAIN'),
}
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL') or 'noreply@example.com'

import django_heroku
django_heroku.settings(locals())
