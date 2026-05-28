import asyncio
import logging

logger = logging.getLogger(__name__)


class ReconnectManager:
    RETRY_DELAY = 5

    async def wait_for_retry(self):
        logger.info(
            "Waiting before reconnect"
        )

        await asyncio.sleep(
            self.RETRY_DELAY
        )

