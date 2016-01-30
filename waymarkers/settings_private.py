DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'waymarkers',
        'OPTIONS': {
            'options': '-c search_path=cms,public'
        },
        'CONN_MAX_AGE': None,
        'USER': 'gis',
        'PASSWORD': 'CorAudralt8',
    },
}
