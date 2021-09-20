# rabbitmq-celery-redis

Purpose:

* Third-party tasks — The web app must serve users quickly without waiting for other actions to complete while the page loads, e.g., sending an email or notification or propagating updates to internal tools (such as gathering data for A/B testing or system logging).
* Long-running jobs — Jobs that are expensive in resources, where users need to wait while they compute their results, e.g., complex workflow execution (DAG workflows), graph generation, Map-Reduce like tasks, and serving of media content (video, audio).
* Periodic tasks — Jobs that you will schedule to run at a specific time or after an interval, e.g., monthly report generation or a web scraper that runs twice a day.

Parts:

* Message broker, message transport: RabbitMQ
* Task worker(s): Celery
* Result store: Redis

## Install

```bash
python -m venv .venv
pip install -r requirements.txt
```

## Run

```bash
# start the broker and redis
docker compose up

# start workers
celery --app tasks worker --loglevel info --queues hello
celery --app tasks worker --loglevel info --queues goodbye

# send tasks
python celery_app.py
```

One worker can process both queues (good for development):

```bash
celery --app tasks worker --loglevel info --queues hello,goodbye
```
