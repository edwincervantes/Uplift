# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Uplift',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'upliftdatabase.cifis9nwmjof.us-east-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}
