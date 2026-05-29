import time


class PacketValidator:
    MAX_TIME_DRIFT = 30

    @staticmethod
    def validate_timestamp(
        timestamp: float
    ) -> bool:
        current = time.time()

        return (
            abs(current - timestamp)
            <= PacketValidator.MAX_TIME_DRIFT
        )

    @staticmethod
    def validate_sequence(
        expected: int,
        received: int
    ) -> bool:
        return expected == received


