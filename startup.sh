#!/bin/bash
celery --app netology worker --loglevel INFO --pool threads --events &> /var/log/celery.log &
python3 -u manage.py runserver --noreload 0.0.0.0:8000
