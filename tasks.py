import asyncio

from celery import Celery

broker_url = "amqp://localhost"
redis_url = "redis://localhost"
app = Celery("tasks", broker=broker_url, backend=redis_url)

app.conf.task_routes = {
    "tasks.say_hello": {"queue": "hello"},
    "tasks.say_goodbye": {"queue": "goodbye"},
}


async def echo_hello(name: str):
    await asyncio.sleep(5)
    return f"Hello {name}"


async def echo_goodbye(name: str):
    await asyncio.sleep(5)
    return f"Goodbye {name}"


@app.task
def say_hello(name: str):
    return asyncio.run(echo_hello(name))


@app.task
def say_goodbye(name: str):
    return asyncio.run(echo_goodbye(name))
