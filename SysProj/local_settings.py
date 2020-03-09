import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'database1': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database1',
        'USER': 'kritesh',
        'PASSWORD': 'Kritesh@123',
        # 'HOST': '',
    },
    'database2': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database2',
        'USER': 'kritesh',
        'PASSWORD': 'Kritesh@123',
        # 'HOST': '',
    },
    'database3': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'database3',
        # 'USER': 'root',
        # 'PASSWORD': 'password',
        # 'HOST': 'localhost',
        # 'PORT': '',
    },
    'database4': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'database4',
        # 'USER': 'root',
        # 'PASSWORD': 'password',
        # 'HOST': 'localhost',
        # 'PORT': '',
    },
    'database5': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'database5',
        # 'USER': 'root',
        # 'PASSWORD': 'password',
        # 'HOST': 'localhost',
        # 'PORT': '',
    }
}
