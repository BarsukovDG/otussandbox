import pytest
import requests

from brewery_info import get_breweries_states
from endpoints import get_brew_endpoints
from lessonApi.brewery_info import get_brewery_types, get_all_breweries
from random import randint


def test_brewery_by_state(brew_base_url):
    states = get_breweries_states(brew_base_url)
    state_randomizer = states[randint(0, len(states) - 1)]
    endpoints = get_brew_endpoints(brewery_state=state_randomizer)
    r = requests.get(f'{brew_base_url}{endpoints["by_state"]}')
    resp_body = r.json()
    assert len(resp_body) > 0
    for i in resp_body:
        assert state_randomizer in i['state']


@pytest.mark.parametrize('brewery_type', get_brewery_types())
def test_brewery_by_type(brew_base_url, brewery_type):
    endpoints = get_brew_endpoints(brewery_type=brewery_type)
    r = requests.get(f'{brew_base_url}{endpoints["by_type"]}')
    resp_body = r.json()
    assert len(resp_body) > 0
