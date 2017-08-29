from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skhufeeds.settings')

app = Celery('skhufeeds')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# Schedule periodic task
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # run every 3600 seconds.
    # Schedule using celery beat
    print("Configuring periodic task")
    from crawlers.record import run_crawler
    sender.add_periodic_task(3600.0, run_crawler.delay(10.0))
