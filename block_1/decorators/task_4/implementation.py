from block_1.common import (
    MyException,
)

def decorator_maker(times, delay):
    """
    Обертка, которая повторяет вызов функции times раз с паузой delay секунд
    Args:
        times: количество повторений
        delay: задержка (с)

    Returns:
        валидное значение (при вызове bool() -> True)
    """
    import time

    def decorator_func(function):
        def wrapper():
            i = 1
            while i <= times:
                try:
                    base_result = function()
                    return base_result
                except Exception:
                    i += 1
                    if i > times:
                        raise MyException(Exception)
                    else:
                        time.sleep(delay)
        return wrapper
    return decorator_func
    raise NotImplementedError

