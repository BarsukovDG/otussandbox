x = 'hello'
y = 'otus'


def test_print_string():
    print(f'{x} {y}!!!')


def test_return_data():
    data = f'{x} {y}!!!'
    return data


test_print_string()
test_return_data()


