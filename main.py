import asyncio

from server.server import AsyncC2Server


async def main():
    server = AsyncC2Server(
        certfile="certs/server.pem",
        keyfile="certs/server.key"
    )

    await server.start(
        host="0.0.0.0",
        port=4444
    )


if __name__ == "__main__":
    asyncio.run(main())


