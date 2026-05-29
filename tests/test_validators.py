import time

from shared.validators import (
    PacketValidator
)


def test_timestamp_validation():
    current = time.time()

    assert (
        PacketValidator
        .validate_timestamp(current)
    )


def test_sequence_validation():
    assert (
        PacketValidator
        .validate_sequence(1, 1)
    )

    assert not (
        PacketValidator
        .validate_sequence(1, 2)
    )


