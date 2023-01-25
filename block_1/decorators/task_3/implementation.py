from block_1.common import (
    some_func,
)
i = 0

def counter(function):
    """
    Обертка для подсчёта количества вызовов обернутой функции.

    Returns:
        int - количество вызовов функции.
    """

    def wrapper():
        global i
        i += 1
        return i

    return wrapper

    raise NotImplementedError
