from block_1.common import (
    factorial,
    MyException,
)

def check_value(function):
    """
    Обертка, проверяющая валидность переданного значения(неотрицательный int).
    В случае валидного значения - передает дальше в функцию,
    в противном случае - выбрасывает исключение MyException.
    """
    def wrapper(num):
        if type(num) == int and num >= 0:
            base_result = function(num)
            return base_result
        else:
            raise MyException(Exception)

    return wrapper
    raise NotImplementedError

"""
def factorial(n):  #функция для проверки
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact"""
"""
decorate = check_value(factorial)
print(decorate(5))"""