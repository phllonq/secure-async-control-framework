from dataclasses import dataclass
import secrets
import time


@dataclass
class Packet:
    version: int = 1
    packet_id: str = None
    packet_type: str = None
    sequence: int = 0
    timestamp: float = None
    nonce: str = None
    data: dict = None

    def __post_init__(self):
        if self.packet_id is None:
            self.packet_id = secrets.token_hex(16)

        if self.timestamp is None:
            self.timestamp = time.time()

        if self.nonce is None:
            self.nonce = secrets.token_hex(12)
