# Позиционные аргументы (обязательные):
def function_positional(a, b, c):
    print(f'a={a}, b={b} and c={c}')


# function_positional(1, 2, "kick")


# Именнованные аргументы (имеющие значение по умолчанию):
def function_named(a=1, b=2):
    print(a, b)


# function_named(b=3)


# Любое количество позиционных аргументов (args, возвращает tuple):
def any_args(*args):
    print(args)


# any_args(1, 2, 3, 4, 5)


# Любое количество именнованных аргументов (kwargs, возвращает dict):
def any_kwargs(**kwargs):
    print(kwargs)


# any_kwargs(tests=10, succeed=9, failed=1)


# Любое количество любых аргументов, с учетом правил (*args, **kwargs)
def any_of_any_arguments(*args, **kwargs):
    print(args, kwargs)


# any_of_any_arguments(1, 2, 3, 4, a=2, b=15, c='letter')


# Распаковка списков args:
def unpacking_args(*args):
    print(f'*** ***')
    print(f'Длина аргумента == {len(args)}')
    print(f'Значение аргумента == {args}')

l = [1, 2, 3] # list
m = 4, 5, 6 # tuple
f = range(3)
# unpacking_args(l) # передается лишь один аргумент - список или кортеж (со всеми своими значениями)
# unpacking_args(*l) # список или кортеж распаковывается и передаются все его значения
# unpacking_args(f)
# unpacking_args(*f)

# Распаковка kwargs:
def unpacking_kwargs(x, y, z, w):
    print(x, y, z, w)

d = {'x':1, 'y':2, 'z':'stringVal', 'w': []}

unpacking_kwargs(**d)

def any_args_action_sum(*args: int):
    sum = 0
    for i in args:
        sum += i
    print(sum)


any_args_action_sum(1, 2, 3, 4, 5)
