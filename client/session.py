import time


class ClientSession:
    def __init__(self):
        self.connected_at = time.time()
        self.last_seen = time.time()

    def update_activity(self):
        self.last_seen = time.time()


