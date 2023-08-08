from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "interview.settings")

app = Celery("interview")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "sync-data-every-five-minutes": {
        "task": "sync_data.tasks.sync_data",
        "schedule": 300.0,  # 5 minutes in seconds
    },
}