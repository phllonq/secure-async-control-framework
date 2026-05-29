import struct


class PacketTransport:
    HEADER_SIZE = 4

    @staticmethod
    def encode(
        payload: bytes
    ) -> bytes:
        return (
            struct.pack(
                "!I",
                len(payload)
            ) + payload
        )

    @staticmethod
    async def receive(
        reader
    ) -> bytes:
        header = await reader.readexactly(
            PacketTransport.HEADER_SIZE
        )

        length = struct.unpack(
            "!I",
            header
        )[0]

        return await reader.readexactly(
            length
        )

