from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "djangoweb800",
        "USER": "postgres",
        "PASSWORD": "postgresql__password",
        "HOST": "postgres",
        "PORT": "5432",
    }
}

LOGGING = {}
