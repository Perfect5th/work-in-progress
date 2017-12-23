"""
Django settings for wip production.
"""
import os

import dj_database_url

from .settings import *

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', SECRET_KEY)

INSTALLED_APPS += ['django.contrib.postgres']

# Update database configuration with $DATABASE_URL
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
