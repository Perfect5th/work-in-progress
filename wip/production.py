"""
Django settings for wip production.
"""
import os

import django_heroku

from .settings import *

# Miscellaneous deploy settings
DEBUG = False
SECURE_HSTS_SECONDS = 31536000  # One year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'

ALLOWED_HOSTS = ['wiki.mitchellburton.ca']

# Use env secret key
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', SECRET_KEY)

# Activate Django-Heroku
django_heroku.settings(locals())
