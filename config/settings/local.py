from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z8=@-ca&+j$q-1^@^s)e8eumj*c7fs07616=mczhsf(cb@qo1p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'imageadmin',
        'USER': 'daniel',
        'PASSWORD': 'localpassword',
        'HOST': 'localhost',
        'PORT': '',
    }
}
