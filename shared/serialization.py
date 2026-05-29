import json

from dataclasses import asdict


class PacketSerializer:
    @staticmethod
    def serialize(packet) -> bytes:
        return json.dumps(
            asdict(packet)
        ).encode()

    @staticmethod
    def deserialize(
        payload: bytes
    ) -> dict:
        return json.loads(
            payload.decode()
        )

