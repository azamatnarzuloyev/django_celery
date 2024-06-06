import os
# CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
# This configures Redis as the datastore between Django + Celery
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_REDIS_URL", default="redis://redis:6379/0")
# if you out to use os.environ the config is:
# CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_REDIS_URL', 'redis://localhost:6379')

# this allows you to schedule items in the Django admin.
# CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers.DatabaseScheduler"
CELERY_RESULT_BACKEND = os.environ.get('RESULT_BACKEND', default="redis://redis:6379/0")