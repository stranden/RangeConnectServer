import json
import aio_pika

class Subscriber:

    def __init__(self, amqp_connection_uri: str) -> None:
        self.amqp_connection_uri = amqp_connection_uri

    async def subscribe_range_events(self, message: dict) -> None:
        connection = await aio_pika.connect(self.amqp_connection_uri)
        queue_name = "shooting_range_events"
        routing_key = queue_name
        async with connection:
            # Creating a channel
            channel = await connection.channel()

            # Declaring queue
            await channel.declare_queue(
                queue_name
            )