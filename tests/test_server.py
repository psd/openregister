from .fixtures import test_client  # noqa


def test_favicon(test_client):  # noqa
    response = test_client.get("/favicon.ico")
    assert response.status == 200


def test_config_json(test_client):  # noqa
    response = test_client.get("/config.json")
    assert response.status == 200
