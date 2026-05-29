from collections import deque


class RetryQueue:
    def __init__(self):
        self.queue = deque()

    def push(
        self,
        item
    ):
        self.queue.append(item)

    def pop(self):
        if not self.queue:
            return None

        return self.queue.popleft()


