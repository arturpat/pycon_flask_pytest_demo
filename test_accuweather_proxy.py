# after pip install pytest - there will be a pretty green button

from unittest.mock import MagicMock, patch, call

import pytest

from accuweather_proxy import AccuweatherProxy


@pytest.fixture
def city_key_expected_response_requests_mock():
    response_mock = MagicMock()
    response_mock.json = MagicMock(return_value=[{"Key": "test_city_key"}])
    requests_mock = MagicMock(return_value=response_mock)
    return requests_mock


@pytest.fixture
def city_key_empty_response_requests_mock():
    response_mock = MagicMock()
    response_mock.json = MagicMock(return_value=[])
    requests_mock = MagicMock(return_value=response_mock)
    return requests_mock


@pytest.fixture
def accu_proxy():
    return AccuweatherProxy(apikey="test_key")


def test_find_city_ok(accu_proxy, city_key_expected_response_requests_mock):
    with patch("requests.request", city_key_expected_response_requests_mock):
        resp = accu_proxy.find_city_key("asdf")
        # TODO: breakpoint here and come up with correct assertions interactively
