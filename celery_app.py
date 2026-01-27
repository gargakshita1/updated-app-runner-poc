from celery import Celery
import time

celery = Celery(
    "worker",
    broker="redis://redis:6379/0",  # or AWS SQS later
    backend="redis://redis:6379/0"
)

@celery.task
def run_background_task():
    print("Background task started")
    time.sleep(10)
    print("Background task completed")
