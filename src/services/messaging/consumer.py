import asyncio
import json
import aio_pika
from aio_pika.abc import AbstractIncomingMessage
from util import *

class Consumer:

    def __init__(self, amqp_connection_uri: str) -> None:
        self.amqp_connection_uri = amqp_connection_uri

    async def callback(self, message: AbstractIncomingMessage) -> None:
        json_body = json.loads(message.body)

        #print(" [x] Received message %r" % message)
        print("Message body is: %r" % json_body)

        print("Before sleep!")
        await asyncio.sleep(5)  # Represents async I/O operations
        print("After sleep!")
        await aio_pika.message.IncomingMessage.ack(message)

    async def consume_range_events(self):
        connection = await aio_pika.connect(self.amqp_connection_uri)
        queue_name = "shooting_range_events"
        async with connection:
            # Creating a channel
            logging.info("Creating RabbitMQ channel")
            channel = await connection.channel()

            # Declaring queue
            logging.info(f"Declaring RabbitMQ queue: {queue_name}")
            queue = await channel.declare_queue(
                queue_name
            )

            # Start listening the queue
            logging.info(f"Starting to consume RabbitMQ queue")
            await queue.consume(self.callback, no_ack=False)

            await asyncio.Future()
