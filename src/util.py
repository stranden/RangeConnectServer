import uuid
import logging
import logging.config
 
def check_shooting_range_id(value):
    try:
        uuid.UUID(value)
        return True
    except ValueError:
        return False

#logger = logging.getLogger(__name__)
#logger.setLevel(level=logging.INFO)
#logger.addHandler(
#    logging.StreamHandler()
#    logging.format("%(asctime)s - [%(levelname)s]: %(message)s")
#)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
