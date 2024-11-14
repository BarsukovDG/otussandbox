import requests

from endpoints import get_dog_endpoints
from lessonApi.conftest import dog_base_url


def get_expected_breeds():
    expected_breeds = ['akita', 'australian', 'corgi', 'husky', 'terrier']
    return expected_breeds


def get_all_breeds(dog_base_url):
    endpoints = get_dog_endpoints()
    breed_list = []
    r = requests.get(f'{dog_base_url}{endpoints["all_breed_list"]}')
    r_body = r.json()
    for i in r_body['message']:
        breed_list.append(i)
    return breed_list