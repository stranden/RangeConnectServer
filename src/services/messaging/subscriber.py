import aio_pika
import asyncio
import json
from aio_pika.abc import AbstractIncomingMessage
from ..database import DBSession, models
from sqlalchemy.orm import Session
from util import logger


class Subscriber:

    def __init__(self, amqp_connection_uri: str) -> None:
        self.amqp_connection_uri = amqp_connection_uri
        logger.debug("Subscriber Class have been created")

    async def proccess_message(self, message: AbstractIncomingMessage) -> None:
        async with message.process(ignore_processed=True):
            db: Session = DBSession()
            range_event = json.loads(message.body)
            
            if range_event.get("scoreEventType") == "ATHLETE":
                if range_event.get("startNumber") != "0":
                    shooter: models.RangeEventShooter = (db.query(models.RangeEventShooter)
                                                            .filter(
                                                                models.RangeEventShooter.shooting_range_id == range_event.get("shootingRangeID"),
                                                                models.RangeEventShooter.firing_point == range_event.get("firingPointID"),
                                                                models.RangeEventShooter.start_number == range_event.get("startNumber"))
                                                            .first())
                    if not shooter:
                        try:
                            db.add(
                                models.RangeEventShooter(
                                    shooting_range_id=range_event.get("shootingRangeID"),
                                    firing_point=range_event.get("firingPointID"),
                                    start_number=range_event.get("startNumber"),
                                    name=range_event.get("name"),
                                    club=range_event.get("team"),
                                    group=range_event.get("group")
                                )
                            )
                            db.commit()
                            logger.info(f"Inserted ATHLETE to DB: {range_event}")
                        finally:
                            db.close()
                            await message.ack()
                    else:
                        logger.info(f"ATHLETE is already in DB")
                else:
                    logger.info(f"ATHLETE is not inserted to DB: {range_event}")

            elif range_event.get("scoreEventType") == "SHOT":
                if range_event.get("startNumber") != "0":
                    try:
                        if range_event.get("series_type") == "SIGHTERS":
                           series_type = models.SeriesType.SIGHT
                        elif range_event.get("series_type") == "MATCH":
                           series_type = models.SeriesType.MATCH
                        elif range_event.get("series_type") == "SHOOTOFF":
                           series_type = models.SeriesType.MATCH
                        db.add(
                            models.RangeEventShot(
                                shooting_range_id=range_event.get("shootingRangeID"),
                                firing_point=range_event.get("firingPointID"),
                                start_number=range_event.get("startNumber"),
                                series_type=series_type,
                                shot_id=range_event.get("shotID"),
                                shot_value=range_event.get("shotValue"),
                                shot_value_decimal=range_event.get("shotValueDecimal"),
                                x_coord=range_event.get("xCoord"),
                                y_coord=range_event.get("yCoord")
                            )
                        )
                        db.commit()
                        logger.info(f"Inserted SHOT to DB: {range_event}")
                    finally:
                        db.close()
                        await message.ack()
                else:
                    logger.info(f"SHOT is not inserted to DB: {range_event}")


    async def subscribe_range_events(self) -> None:
        connection = await aio_pika.connect(self.amqp_connection_uri)
        queue_name = "shooting_range_events"
        async with connection:
            logger.debug("Established connection to RabbitMQ")
            # Creating a channel
            channel = await connection.channel()

            # Declaring queue
            queue = await channel.declare_queue(
                queue_name,
                durable=True
            )

            # Consume messages
            await queue.consume(self.proccess_message)
            
            try:
                # Wait until terminate
                await asyncio.Future()
            finally:
                await connection.close()
                