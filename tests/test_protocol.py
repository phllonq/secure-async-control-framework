from shared.protocol import Packet


def test_packet_creation():
    packet = Packet(
        packet_type="heartbeat"
    )

    assert packet.packet_type == (
        "heartbeat"
    )

    assert packet.packet_id is not None

    assert packet.nonce is not None


