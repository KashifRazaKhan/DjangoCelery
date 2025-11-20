from celery import shared_task

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
