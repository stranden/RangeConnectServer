import asyncio
import settings
import services.messaging.consumer
from util import *

async def main() -> None:

    logging.info("Starting RangeConnectServer")
    logging.info("Creating RabbitMQ consumer task")

    Consumer = services.messaging.consumer.Consumer(settings.RABBITMQ_URI)


    task_consume = asyncio.create_task(
            Consumer.consume_range_events()
        )

    logging.info("Executing RabbitMQ consumer task")
    await task_consume

if __name__ == "__main__":
    asyncio.run(main())