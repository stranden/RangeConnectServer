import asyncio
import settings
import services.messaging.subscriber
from util import logger

async def rabbitmq_subscriber():
    logger.debug("Reached the rabbitmq_subscriber function")
    Subscriber = services.messaging.subscriber.Subscriber(settings.RABBITMQ_URI)

    while(True):
        await Subscriber.subscribe_range_events()
        logger.debug("While loop is running")

async def main():
    logger.info("Starting RangeConnectServer")

    logger.info("Creating RabbitMQ subscriber task")
    task_rabbitmq_subscriber = asyncio.create_task(
       rabbitmq_subscriber()
    )

    logger.info("Executing RabbitMQ subscriber task")
    await task_rabbitmq_subscriber

asyncio.run(main())