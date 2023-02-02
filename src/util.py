import uuid
import logging
 
def check_shooting_range_id(value):
    try:
        uuid.UUID(value)
        return True
    except ValueError:
        return False

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)
consoleFormatter = logging.Formatter("%(asctime)s - [%(levelname)s]: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
consoleHandler.setFormatter(consoleFormatter)
logger.addHandler(consoleHandler)
