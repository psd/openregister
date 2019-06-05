import requests_mock
from openregister.client import RegisterClient


def test_client_url():
    client = RegisterClient()
    assert client is not None

    with requests_mock.Mocker() as mock:
        mock.get("https://example.com", text="data")
        assert "data" == client.get("https://example.com").text
