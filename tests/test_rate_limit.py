from server.rate_limit import (
    RateLimiter
)


def test_rate_limiter():
    limiter = RateLimiter()

    for _ in range(10):
        assert limiter.allow()

