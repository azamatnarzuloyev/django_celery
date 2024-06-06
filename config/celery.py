import os 
from celery import Celery
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery('config')
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.task_routes = {'newsapps.tasks.task1':{"queue": "queue1"},  'newsapps.tasks.task2': {"queue": "queue2"}}

app.autodiscover_tasks()