import aio_pika
import asyncio
import json
from util import logger
from aio_pika.abc import AbstractIncomingMessage

class Subscriber:

    def __init__(self, amqp_connection_uri: str) -> None:
        self.amqp_connection_uri = amqp_connection_uri
        logger.debug("Subscriber Class have been created")

    async def proccess_message(self, message: AbstractIncomingMessage) -> None:
        async with message.process(ignore_processed=True):
            logger.info(f"Consumed message: {json.loads(message.body)}")
            await asyncio.sleep(1)
            await message.ack()

    async def subscribe_range_events(self) -> None:
        connection = await aio_pika.connect(self.amqp_connection_uri)
        queue_name = "shooting_range_events"
        async with connection:
            logger.debug("Established connection to RabbitMQ")
            # Creating a channel
            channel = await connection.channel()

            # Declaring queue
            queue = await channel.declare_queue(
                queue_name
            )

            # Consume messages
            await queue.consume(self.proccess_message)
            
            try:
                # Wait until terminate
                await asyncio.Future()
            finally:
                await connection.close()
                