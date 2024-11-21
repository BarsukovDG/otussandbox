import pytest
import requests

from brewery_info import get_breweries_states
from endpoints import get_brew_endpoints
from lessonApi.brewery_info import get_brewery_types, get_all_breweries, get_brewery_keys
from random import randint


def test_get_single_brewery(brew_base_url):
    endpoints = get_brew_endpoints()
    brewery_keys = get_brewery_keys()
    r = requests.get(f'{brew_base_url}{endpoints["single_brewery"]}')
    resp_body = r.json()
    for k, v in resp_body.items():
        assert k in brewery_keys


@pytest.mark.parametrize('brewery', get_all_breweries())
def test_get_all_breweries(brew_base_url, brewery):
    breweries_keys = get_brewery_keys()
    for i in brewery:
        assert i in breweries_keys, f'there is no "{i}" key in expected list'


@pytest.mark.parametrize('brewery_type', get_brewery_types())
def test_get_brewery_by_type(brew_base_url, brewery_type):
    endpoints = get_brew_endpoints(brewery_type=brewery_type)
    r = requests.get(f'{brew_base_url}{endpoints["by_type"]}')
    resp_body = r.json()
    assert len(resp_body) > 0


def test_get_brewery_random(brew_base_url):
    endpoints = get_brew_endpoints()
    brewery_keys = get_brewery_keys()
    r1 = requests.get(f'{brew_base_url}{endpoints["random_brewery"]}')
    r2 = requests.get(f'{brew_base_url}{endpoints["random_brewery"]}')
    resp1_body = r1.json()
    resp2_body = r2.json()
    assert resp1_body != resp2_body, ('There is little chance possibility to get same brewery by random twice in a row.'
                                      'If this assertion failed try again to check this test relevance')
    for item in resp1_body:
        for k, v in item.items():
            assert k in brewery_keys
            print(f'{k} ___AND___ {v}') #TODO del this print after fixing raiseException
            with pytest.raises(Exception), f'there is no value for key "{k}" in brewery {item["name"]}':
                assert v


def test_get_brewery_by_state(brew_base_url):
    states = get_breweries_states(brew_base_url)
    state_randomizer = states[randint(0, len(states) - 1)]
    endpoints = get_brew_endpoints(brewery_state=state_randomizer)
    r = requests.get(f'{brew_base_url}{endpoints["by_state"]}')
    resp_body = r.json()
    assert len(resp_body) > 0
    for i in resp_body:
        assert state_randomizer in i['state'], f'there is no breweries in "{state_randomizer}" state'
