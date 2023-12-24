from os import environ

from celery import Celery
from django.conf import settings

environ.setdefault("DJANGO_SETTINGS_MODULE", "netology.settings")


def create_application(namespace):
    celery = Celery(__package__)
    celery.config_from_object(settings, namespace=namespace)
    celery.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
    return celery


application = create_application(namespace="CELERY")
