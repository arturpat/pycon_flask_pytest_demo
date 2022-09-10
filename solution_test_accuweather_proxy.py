# 1. Unit tests evangelisation
# after pip install - pretty green button

from unittest.mock import MagicMock, patch, call

import pytest

from solution_accuweather_proxy import AccuweatherProxy


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

        # to be written live:
        assert resp == "test_city_key"
        city_key_expected_response_requests_mock.assert_called()
        city_key_expected_response_requests_mock.assert_called_once()
        assert city_key_expected_response_requests_mock.call_count == 1
        # see city_key_expected_response_requests_mock.mock_calls[0][1:3]
        call()  # alt+enter
        assert call("POST", "http://dataservice.accuweather.com/locations/v1/cities/search",
                    params={"apikey": "test_key", "q": "asdf"}) in city_key_expected_response_requests_mock.mock_calls


    pass

# backup: handle empty return list in a new test ("not ok")
