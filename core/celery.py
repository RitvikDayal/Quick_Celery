from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from datetime import timedelta

# os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'send_email_every_5_minute': {
        'task': 'send_contact_message_task',
        'schedule': timedelta(seconds=30),
    }
} 
app.conf.timezone = 'UTC'

app.autodiscover_tasks()

'''
Command to run Celery **Windows**:
celery -A [app name] worker -l info --pool=solo

Command to run Celery **Linux**:
celery -A [app name] worker -l info
'''