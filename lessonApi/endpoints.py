def get_dog_endpoints(breed='hound'):
    """
    return dict of endpoints with opportunity to choose breed for specific requests
    """
    endpoints = {
        'all_breed_list': '/api/breeds/list/all',
        'random_image': '/api/breeds/image/random',
        'images_by_breed': f'/api/breed/{breed}/images',
        'random_image_by_breed': f'/api/breed/{breed}/images/random',
        'sub_breeds_by_breed': f'/api/breed/{breed}/list',
        'browse_breed_list_random_image': f'/api/breed/{breed}/images/random'
    }
    return endpoints


def get_brew_endpoints(brewery_type=None, brewery_state=None):
    endpoints = {
        'single_brewery': '/v1/breweries/{obdb-id}',
        'all_breweries': '/v1/breweries',
        'by_type': f'/v1/breweries?by_type={brewery_type}',
        'random_brewery': '/v1/breweries/random',
        'by_state': f'/v1/breweries?by_state={brewery_state}'
    }
    return endpoints
