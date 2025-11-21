from django.urls import path
from .views import (index,
                    failure_view,
                    start_task,
                    task_status )

urlpatterns = [
    path('', index, name='index'),
    path('failure/', failure_view, name='failure'),
    path('start-task/', start_task, name='start-task'),
    path('task-status/<str:task_id>/', task_status, name='task-status'),
]