import os
ROOT_URLCONF = 'buildup.urls'
WSGI_APPLICATION = 'buildup.wsgi.application'
SECRET_KEY = os.environ['DJANGO_SECRET']
DEBUG = 'DEBUG' in os.environ
