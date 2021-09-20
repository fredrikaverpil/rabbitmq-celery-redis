from time import sleep

from tasks import say_hello, say_goodbye

from loguru import logger
from faker import Faker


def send_hello(name):
    result = say_hello.delay(name)
    logger.info(result.status)

    # # Un-comment to wait for the result
    # while result.status == "PENDING":
    #     logger.info(f"Result status: {result.status}")
    #     sleep(1)
    # logger.info(f"Result status: {result.status}")
    # logger.info(f"Result: {result.get()}")
    # return result.get()


def send_goodbye(name):
    result = say_goodbye.delay(name)
    logger.info(result.status)

    # # Un-comment to wait for the result
    # while result.status == "PENDING":
    #     logger.info(f"Result status: {result.status}")
    #     sleep(1)
    # logger.info(f"Result status: {result.status}")
    # logger.info(f"Result: {result.get()}")
    # return result.get()


def main():
    fake = Faker()
    name = str(fake.name())
    send_hello(name)
    send_goodbye(name)


if __name__ == "__main__":
    main()
