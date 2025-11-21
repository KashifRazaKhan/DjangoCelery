from celery import shared_task, chain, chord
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

@shared_task
def task_add(x):
    return x + 10

@shared_task
def task_double(y):
    return y * 2

@shared_task
def task_subtract(z):
    return z - 3

def workflow_chain(start_num):
    job = chain(
        task_add.s(start_num),
        task_double.s(),
        task_subtract.s()
    )
    return job.apply_async()

@shared_task
def process_item(x):
    return x * 2

@shared_task
def combine(results):
    return sum(results)

def workflow_chord(numbers):
    header = [process_item.s(n) for n in numbers]
    callback = combine.s()
    return chord(header)(callback)