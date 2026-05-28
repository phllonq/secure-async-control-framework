import asyncio
import logging

from client.transport import TransportLayer
from client.heartbeat import HeartbeatManager

logger = logging.getLogger(__name__)


class AsyncClient:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

        self.transport = TransportLayer(
            host=self.host,
            port=self.port
        )

        self.heartbeat = HeartbeatManager()

    async def start(self):
        logger.info("Starting client")

        await self.transport.connect()

        asyncio.create_task(
            self.heartbeat.start()
        )

        await self.listen()

    async def listen(self):
        while True:
            packet = await self.transport.receive()

            if not packet:
                break

            logger.info("Packet received")

