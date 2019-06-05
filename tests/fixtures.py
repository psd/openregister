import pytest
from openregister.server import RegisterServer


class TestClient:
    def __init__(self, sanic_test_client):
        self.sanic_test_client = sanic_test_client

    def get(self, path, allow_redirects=True):
        return self.sanic_test_client.get(
            path, allow_redirects=allow_redirects, gather_request=False
        )


def make_test_client():
    server = RegisterServer()
    client = TestClient(server.server().test_client)
    client.server = server
    yield client


@pytest.fixture(scope="session")
def test_client():
    yield from make_test_client()
