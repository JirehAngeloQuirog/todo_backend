from dotenv import load_dotenv
import os
from pathlib import Path
import dj_database_url


load_dotenv()


# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key and debug flag
SECRET_KEY = os.getenv('SECRET_KEY', 'JirehQuirog')
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Allowed hosts for Render
ALLOWED_HOSTS = ['todobackend-h9se.onrender.com', '127.0.0.1', 'localhost']

# CORS (for GitHub Pages frontend)
CORS_ALLOWED_ORIGINS = [
    "https://jirehangeloquirog.github.io",
    "https://snack.expo.dev/@jquirog/b73319",
]

CORS_ALLOW_ALL_ORIGINS = False

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'todoapi.apps.TodoapiConfig',
    'corsheaders',
    'whitenoise.runserver_nostatic',
    'rest_framework.authtoken',
]

# Middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# REST framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',  # Needed for browser login
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}




# URL and template settings
ROOT_URLCONF = 'todobackend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'todobackend.wsgi.application'

# Database setup: PostgreSQL on Render, fallback to SQLite locally
DATABASE_URL = os.getenv('DATABASE_URL')

if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=600, ssl_require=True)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'quirog-todobackend',  # Replace with your DB name
            'USER': 'quirog_todobackend_user',  # Replace with your DB username
            'PASSWORD': 'tI1A62gDv1g3JfZpFe7v3NZhF4wvcIK1',  # Replace with your DB password
            'HOST': 'dpg-cvppg895pdvs73ed9bmg-a',  # Replace with your DB host (e.g., localhost or Render DB host)
            'PORT': '5432',  # Default PostgreSQL port
        }
    }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Localization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files setup
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
