from django.urls import path
from .views import (index,
                    failure_view,
                    start_task,
                    task_status,
                    run_chain_view,
                    run_chord_view
                    )

urlpatterns = [
    path('', index, name='index'),
    path('failure/', failure_view, name='failure'),
    path('start-task/', start_task, name='start-task'),
    path('task-status/<str:task_id>/', task_status, name='task-status'),
    path("run-chain/", run_chain_view ),
    path("run-chord/", run_chord_view),

]