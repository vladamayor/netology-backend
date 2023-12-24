import os
from datetime import timedelta

from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "=hs6$#5om031nujz4staql9mbuste=!dc^6)4opsjq!vvjxzj@"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "django_rest_passwordreset",
    "netology",
    "netology.backend",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "netology.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "netology.wsgi.application"

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"

AUTH_USER_MODEL = "netology.User"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_USE_TLS = True

EMAIL_HOST = "smtp.yandex.ru"

EMAIL_HOST_USER = "vladamayor@yandex.ru"
EMAIL_HOST_PASSWORD = os.environ["PASS"]
EMAIL_PORT = 465
EMAIL_USE_SSL = True
SERVER_EMAIL = EMAIL_HOST_USER

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 40,
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
    ),
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Celery Settings:

# https://docs.celeryproject.org/en/stable/userguide/configuration.html#accept-content
# https://docs.celeryproject.org/en/stable/userguide/configuration.html#result-accept-content
CELERY_ACCEPT_CONTENT = ["json", "pickle"]
CELERY_RESULT_ACCEPT_CONTENT = CELERY_ACCEPT_CONTENT.copy()

# https://docs.celeryproject.org/en/stable/userguide/configuration.html#task-compression
# https://docs.celeryproject.org/en/stable/userguide/configuration.html#result-compression
CELERY_TASK_COMPRESSION = "lzma"
CELERY_RESULT_COMPRESSION = CELERY_TASK_COMPRESSION

# https://docs.celeryproject.org/en/stable/userguide/configuration.html#task-serializer
# https://docs.celeryproject.org/en/stable/userguide/configuration.html#result-serializer
CELERY_TASK_SERIALIZER = "pickle"
CELERY_RESULT_SERIALIZER = CELERY_TASK_SERIALIZER

# https://docs.celeryproject.org/en/stable/userguide/configuration.html#task-ignore-result
CELERY_TASK_IGNORE_RESULT = True

# https://docs.celeryproject.org/en/stable/userguide/configuration.html#task-soft-time-limit
CELERY_TASK_SOFT_TIME_LIMIT = timedelta(minutes=5).total_seconds()

# https://docs.celeryproject.org/en/stable/userguide/configuration.html#result-backend
CELERY_RESULT_BACKEND = "rpc://"

# https://docs.celeryproject.org/en/stable/userguide/configuration.html#broker-url
CELERY_BROKER_URL = "amqp://guest:guest@127.0.0.1:9000"
