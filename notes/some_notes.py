from re import split


def factorial(n):
    """
    Факториал числа - умножение всех чисел до выбранного числа
    """
    factorial = 1
    while n >= 1:
        factorial *= n
        n -= 1
    # return factorial
    print(factorial)


factorial(5)


def list_comprehension():
    """
    Генератор списков (упрощенная форма цикла for)
    """
    a = [i * i for i in range(10)]
    # return a
    print(a)


# list_comprehension()


def gen(n):
    """
    Генератор - это функция, которая используется для генерации
    бесконечных последовательностей, итерации по большим данным etc.,
    в которой можно приостановить и продолжить ее выполнение.
    Внутри нее вместо return используется yield.
    Нужна как lazy итератор, чтобы более эффективно использовать память.
    """
    for i in range(n):
        yield i


# gen(7)


"""
lambda func
"""
double = lambda x: x * 2
multiply = lambda x, y: x * y
square = lambda x: x * x

# print(multiply(4, 8))

"""
splitting
"""


def split_sentence_word_by_word(word_index: int):
    sentence = 'У меня есть самый надежный и лучший друг на свете'
    print(sentence.split(' ')[word_index])

# split_sentence_word_by_word(4)
