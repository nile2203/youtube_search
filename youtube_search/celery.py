from __future__ import absolute_import, unicode_literals

import celery
import os

from celery import Celery

from fampay.settings import CELERY_BROKER_URL

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fampay.settings')


class BaseTask(celery.Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('Task failed')

    def on_success(self, retval, task_id, args, kwargs):
        return retval


app = Celery('youtube_search',
             broker=CELERY_BROKER_URL,
             backend='amqp',
             include=['youtube_search.videos.tasks'],
             task_cls=BaseTask)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

