from time import sleep

from tasks import say_hello

from loguru import logger


def main():
    result = say_hello.delay("Hello, World!")
    logger.info(result.status)

    while result.status == "PENDING":
        logger.info(f"Result status: {result.status}")
        sleep(1)

    logger.info(f"Result status: {result.status}")
    logger.info(f"Result: {result.get()}")


if __name__ == "__main__":
    main()
