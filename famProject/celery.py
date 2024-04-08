# celery.py (in your Django project directory)
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'famProject.settings')

app = Celery('famProject')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.broker_connection_retry_on_startup = True

app.conf.beat_schedule = {
    'fetch_youtube_videos': {
        'task': 'Youtube.tasks.store_video_data',
        'schedule': 10.0  # It will run every 10 seconds
    }
}
