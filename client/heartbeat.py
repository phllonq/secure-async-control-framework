import asyncio
import logging

logger = logging.getLogger(__name__)


class HeartbeatManager:
    INTERVAL = 30

    async def start(self):
        while True:
            logger.info("Heartbeat transmitted")

            await asyncio.sleep(
                self.INTERVAL
            )


