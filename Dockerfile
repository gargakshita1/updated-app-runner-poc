FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Start both FastAPI and Celery together
CMD uvicorn main:app --host 0.0.0.0 --port 8000 & \
    celery -A celery_app.celery worker --loglevel=info

