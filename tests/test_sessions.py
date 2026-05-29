from server.session import (
    ClientSession
)


def test_session_creation():
    session = ClientSession(
        client_id="client-1"
    )

    assert (
        session.client_id
        == "client-1"
    )

    assert session.sequence == 0


def test_sequence_increment():
    session = ClientSession(
        client_id="client-1"
    )

    value = session.next_sequence()

    assert value == 1

