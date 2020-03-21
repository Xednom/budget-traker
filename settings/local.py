from .base import *

DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT'),
    }
}

# see https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_ROOT = (
    os.path.join(BASE_DIR, 'staticfiles')
)
