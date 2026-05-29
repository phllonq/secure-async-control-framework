import time
from collections import deque


class RateLimiter:
    LIMIT = 100
    WINDOW = 60

    def __init__(self):
        self.requests = deque()

    def allow(self) -> bool:
        now = time.time()

        while (
            self.requests and
            self.requests[0] < now - self.WINDOW
        ):
            self.requests.popleft()

        if len(self.requests) >= self.LIMIT:
            return False

        self.requests.append(now)

        return True


