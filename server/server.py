import asyncio
import logging
import ssl

logger = logging.getLogger(__name__)


class AsyncC2Server:
    def __init__(
        self,
        certfile: str,
        keyfile: str
    ):
        self.certfile = certfile
        self.keyfile = keyfile

        self.ssl_context = (
            ssl.create_default_context(
                ssl.Purpose.CLIENT_AUTH
            )
        )

        self.ssl_context.load_cert_chain(
            certfile=self.certfile,
            keyfile=self.keyfile
        )

    async def start(
        self,
        host: str,
        port: int
    ):
        server = await asyncio.start_server(
            self.handle_client,
            host,
            port,
            ssl=self.ssl_context
        )

        logger.info(
            f"Listening on {host}:{port}"
        )

        async with server:
            await server.serve_forever()

    async def handle_client(
        self,
        reader,
        writer
    ):
        peer = writer.get_extra_info(
            "peername"
        )

        logger.info(
            f"Client connected: {peer}"
        )

        try:
            while True:
                data = await reader.read(4096)

                if not data:
                    break

                logger.info(
                    f"Received {len(data)} bytes"
                )

        finally:
            writer.close()

            await writer.wait_closed()

