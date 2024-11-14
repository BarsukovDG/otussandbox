import pytest
import requests

from endpoints import get_dog_endpoints
from breed_info import get_expected_breeds, get_all_breeds


def check_success_statuscode(response):
    assert response.status_code in range(200, 299)


def test_breed_list(dog_base_url):
    endpoints = get_dog_endpoints()
    r = requests.get(f'{dog_base_url}{endpoints["all_breed_list"]}')
    response_body = r.json()
    check_success_statuscode(r)
    for breed in get_expected_breeds():
        assert breed in response_body['message']
    assert 'success' in response_body['status']


def test_random_image(dog_base_url):
    endpoints = get_dog_endpoints()
    r1 = requests.get(f'{dog_base_url}{endpoints["random_image"]}')
    r2 = requests.get(f'{dog_base_url}{endpoints["random_image"]}')
    body1 = r1.json()
    body2 = r2.json()
    assert body1 != body2
    assert 'success' in body1['status'] and 'success' in body2['status']
    assert '.jpg' in body1['message']


@pytest.mark.parametrize("breed", get_expected_breeds())
def test_images_by_breed(dog_base_url, breed):
    endpoints = get_dog_endpoints(breed=breed)
    r1 = requests.get(f'{dog_base_url}{endpoints["images_by_breed"]}')
    r2 = requests.get(f'{dog_base_url}{endpoints["random_image_by_breed"]}')
    body1 = r1.json()
    body2 = r2.json()
    check_success_statuscode(r1)
    check_success_statuscode(r2)
    assert len(body1['message']) > 1
    assert 'success' in body1['status']
    assert '.jpg' in body2['message']
    assert type(body2['message']) is not list


@pytest.mark.parametrize("breed", get_expected_breeds())
def test_sub_breeds(dog_base_url, breed):
    endpoints = get_dog_endpoints(breed)
    all_breeds = get_all_breeds(dog_base_url)
    if breed not in all_breeds:
        raise Exception(
            f"Please, choose one of existing breeds. There is no {breed} in this list")
    else:
        r = requests.get(f'{dog_base_url}{endpoints["sub_breeds_by_breed"]}')
        resp_body = r.json()
        if not resp_body['message']:
            print(f'Request is succeed, just there is no subbreed for this breed: {breed}')
            check_success_statuscode(r)
        else:
            assert resp_body['message']
        assert resp_body['status'] == 'success'


@pytest.mark.parametrize("breed", get_expected_breeds())
def test_browse_random_image(dog_base_url, breed):
    endpoints = get_dog_endpoints(breed)
    r = requests.get(f'{dog_base_url}{endpoints["browse_breed_list_random_image"]}')
    resp_body = r.json()
    check_success_statuscode(r)
    assert '.jpg' in resp_body['message']
