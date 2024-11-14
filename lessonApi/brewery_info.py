import requests

from endpoints import get_brew_endpoints


def get_all_breweries(brew_base_url):
    endpoints = get_brew_endpoints()
    r = requests.get(f'{brew_base_url}{endpoints["all_breweries"]}')
    resp_body = r.json()
    return resp_body


def get_breweries_states(brew_base_url):
    all_breweries = get_all_breweries(brew_base_url)
    breweries_state_list = []
    for i in all_breweries:
        if i['state'] not in breweries_state_list:
            breweries_state_list.append(i['state'])
    return breweries_state_list


def get_brewery_types(brew_base_url='https://api.openbrewerydb.org'):
    all_breweries = get_all_breweries(brew_base_url)
    brewery_types_list = []
    for i in all_breweries:
        if i['brewery_type'] not in brewery_types_list:
            brewery_types_list.append(i['brewery_type'])
    return brewery_types_list
