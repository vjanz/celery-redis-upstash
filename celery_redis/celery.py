import os
import time
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celery_redis.settings")  # Update with your project's settings module
app = Celery("celery_redis")  # Update with your project name
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.task
def reverse_and_sleep(input_string, sleep_duration):
    reversed_string = input_string[::-1]
    time.sleep(sleep_duration)
    return reversed_string
