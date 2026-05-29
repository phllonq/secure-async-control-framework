import time


class ClientSession:
    def __init__(
        self,
        client_id: str
    ):
        self.client_id = client_id

        self.connected_at = time.time()
        self.last_seen = time.time()

        self.sequence = 0

    def touch(self):
        self.last_seen = time.time()

    def next_sequence(self):
        self.sequence += 1

        return self.sequence


