import time
from collections import deque


class RateLimitError(Exception):
    pass


class MockAPI:
    def __init__(self):
        self.call_times = deque()

    def call(self, prompt: str) -> str:
        now = time.time()
        while self.call_times and now - self.call_times[0] > 5:
            self.call_times.popleft()
        if len(self.call_times) >= 5:
            raise RateLimitError("Too many requests in 5 seconds.")
        self.call_times.append(now)
        return f"Response for: {prompt}"
