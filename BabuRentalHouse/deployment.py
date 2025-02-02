from .settings import *
import os 
from .settings import BASE_DIR
import dj_database_url


DEBUG = False

ALLOWED_HOSTS = [os.environ.get('RENDER_EXTERNAL_HOSTNAME')]

CSRF_TRUSTED_ORIGINS = ['https://' + os.environ.get('RENDER_EXTERNAL_HOSTNAME')]

SECRET_KEY = os.environ.get('SECRET_KEY')



MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

CORS_ALLOWED_ORIGINS = [
    "https://ambitious-pebble-06c2dd003.4.azurestaticapps.net",
]
   
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}



DATABASES = {
  'default': dj_database_url.config(
        default=os.environ.get["DATABASE_URL"],
        conn_max_age=600
  )
}

STATIC_ROOT =  BASE_DIR / 'staticfiles'


