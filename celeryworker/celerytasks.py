from celery import Celery

app = Celery('task')
app.config_from_object('celeryconfig')
# app.conf.imports=('newsapps.tasks')

app.autodiscover_tasks()
# fdfdfdfdf
