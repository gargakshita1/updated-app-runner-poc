import logging
from fastapi import FastAPI
from celery_app import run_background_task

logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.get("/")
def health():
    return {"status": "running"}

@app.post("/run-task")
def run_task():
    logging.info("Triggering background task")
    run_background_task.delay()
    return {"message": "Task started"}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)




