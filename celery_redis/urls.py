from django.http import HttpResponse
from celery_redis.celery import reverse_and_sleep
from django.urls import path


def trigger_task(request):
    result = reverse_and_sleep.delay("Hello, Celery!", 10)
    return HttpResponse(f"Task triggered. Task ID: {result.id}")


def get_result(request, task_id):
    result = reverse_and_sleep.AsyncResult(task_id)
    if result.ready():
        return HttpResponse(f"Task result: {result.result}")
    else:
        return HttpResponse(f"Task not finished yet.. Status is: {result.status} ")


urlpatterns = [
    path('trigger-task/', trigger_task, name='trigger_task'),
    path('get-result/<str:task_id>/', get_result, name='get_result'),
]
