from fastapi import FastAPI
from celery_app import run_background_task

app = FastAPI()

@app.get("/")
def health():
    return {"status": "running"}

@app.post("/run-task")
def run_task():
    run_background_task.delay()
    return {"message": "Task started"}



