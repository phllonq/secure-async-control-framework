import asyncio
import ssl
import logging

logger = logging.getLogger(__name__)


class TransportLayer:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

        self.reader = None
        self.writer = None

    async def connect(self):
        ssl_context = ssl.create_default_context()

        self.reader, self.writer = await asyncio.open_connection(
            self.host,
            self.port,
            ssl=ssl_context
        )

        logger.info(
            f"Connected to {self.host}:{self.port}"
        )

    async def send(self, data: bytes):
        self.writer.write(data)
        await self.writer.drain()

    async def receive(self):
        return await self.reader.read(4096)

    async def close(self):
        if self.writer:
            self.writer.close()
            await self.writer.wait_closed()


