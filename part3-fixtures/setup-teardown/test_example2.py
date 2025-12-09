import pytest


class FakeDBConnection:
    def __init__(self):
        self.connected = False

    def connect(self):
        self.connected = True
        print("[Setup] Connected to fake DB")

    def close(self):
        self.connected = False
        print("[Teardown] Closed fake DB connection")

    def fetch_user(self):
        if not self.connected:
            raise RuntimeError("Not connected to DB")
        return {"id": 1, "name": "Alice"}


@pytest.fixture
def db_connection():
    db = FakeDBConnection()
    db.connect()
    yield db
    db.close()


def test_fetch_user(db_connection):
    user = db_connection.fetch_user()
    assert user["name"] == "Alice"


def test_connection_is_active(db_connection):
    assert db_connection.connected is True
