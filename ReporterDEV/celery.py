import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ReporterDEV.settings.local')


app = Celery('ReporterDEV')

app.config_from_object("django.conf:settings", namespace="CELERY")

if os.name == 'nt':
    app.conf.worker_pool = 'solo'

app.autodiscover_tasks()
