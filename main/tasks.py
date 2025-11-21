from celery import shared_task
import time

@shared_task
def add(x, y):
    return x + y

@shared_task
def say_hello():
    print("Hello, Kashif!")

@shared_task(bind=True, default_retry_delay=5, max_retries=3)
def fail(self):
    try:
        raise Exception("Intentional Exception.")
    except Exception as e:
        self.retry(exc=e)

@shared_task(bind=True)
def long_running_task(self, total=10):

    for i in range(1, total + 1):
        time.sleep(1)

        self.update_state(
            state="PROGRESS",
            meta={
                "current": i,
                "total": total,
                "percent": round((i / total) * 100, 2)
            }
        )

    return {
        "status": "completed",
        "total": total
    }
