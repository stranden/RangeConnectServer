import asyncio
from asyncore import loop
import settings
from util import *

async def main():
    logging.info("Starting RangeConnectServer")

asyncio.run(main())