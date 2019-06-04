# import pytest
from openregister.client import RegisterClient


def test_client_url():
    client = RegisterClient()
    assert client is not None


#
# @pytest.fixture
# def requests():
#    return requests.get("data")
#
#
# def test_get_register_register(get):
#    url = "http://www.example.com/"
#    text = 'example data'
#    #mock.get(url, text=text)
#    # client = Client()
#    assert text == requests.get(url).text
