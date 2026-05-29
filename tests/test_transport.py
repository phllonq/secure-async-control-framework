from server.transport import (
    PacketTransport
)


def test_transport_encoding():
    payload = b"hello"

    encoded = (
        PacketTransport
        .encode(payload)
    )

    assert isinstance(
        encoded,
        bytes
    )

    assert len(encoded) > len(
        payload
    )


