import json
import asyncio
import aio_pika
from aio_pika.abc import AbstractIncomingMessage


class Subscriber:

    def __init__(self, amqp_connection_uri: str) -> None:
        self.amqp_connection_uri = amqp_connection_uri

    async def proccess_message(message: AbstractIncomingMessage) -> None:
        async with message.process():
            print(message.body)
            await asyncio.sleep(1)

    async def subscribe_range_events(self) -> None:
        connection = await aio_pika.connect(self.amqp_connection_uri)
        queue_name = "shooting_range_events"
        async with connection:
            # Creating a channel
            channel = await connection.channel()
            await channel.set_qos(prefetch_count=1)

            # Declaring queue
            queue = await channel.declare_queue(
                queue_name,
                durable=True
            )

            # Consume messages
            await queue.consume(proccess_message)