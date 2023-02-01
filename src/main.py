import asyncio
import settings
import services.messaging.subscriber
from util import *

async def rabbitmq_subscriber():
    logging.debug("Reached the rabbitmq_subscriber function")
    Subscriber = services.messaging.subscriber.Subscriber(settings.RABBITMQ_URI)

    while(True):
        await Subscriber.subscribe_range_events()
        logging.debug("While loop is running")

async def main():
    logging.info("Starting RangeConnectServer")

    logging.info("Creating RabbitMQ subscriber task")
    task_rabbitmq_subscriber = asyncio.create_task(
       rabbitmq_subscriber()
    )

    logging.info("Executing RabbitMQ subscriber task")
    await task_rabbitmq_subscriber

asyncio.run(main())