from django.http import JsonResponse
from .tasks import add, fail, long_running_task
from celery.result import AsyncResult

# Create your views here.
def index(request):
    add.delay(2, 9)
    return JsonResponse({"message":"Hello, world! You're at the main index. Shortly you will receive the sum of 2 and 9"})

def failure_view(request):
    fail.delay()
    return JsonResponse({"message":"Something went wrong"})


def start_task(request):
    task = long_running_task.delay(total=20)
    return JsonResponse({"task_id": task.id})

def task_status(request, task_id):
    result = AsyncResult(task_id)

    if result.state == "PENDING":
        return JsonResponse({"state": "PENDING", "progress": 0})

    if result.state == "PROGRESS":
        return JsonResponse({
            "state": result.state,
            "current": result.info.get("current"),
            "total": result.info.get("total"),
            "percent": result.info.get("percent"),
        })

    if result.state == "SUCCESS":
        return JsonResponse({
            "state": "SUCCESS",
            "result": result.get()
        })

    return JsonResponse({"state": result.state, "error": str(result.info)})
