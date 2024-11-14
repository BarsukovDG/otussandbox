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