from random import randint


def print_decorator(func):
    def wrapper():
        print(f'This is what you want to print: {func()}')

    return wrapper


@print_decorator
def random_int():
    return randint(1, 10)


@print_decorator
def string_returning():
    return 'hello world'


string_returning()
