import time


def benchmark(func):
    """
    Враппер для подсчета времени выполнения функции
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        t = end - start
        print("Время выполнения:", t)
        return result

    return wrapper
