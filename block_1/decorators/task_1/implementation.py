def time_execution(function):
    """
    Обертка, печатающая время выполнения функции.
    """
    def wrapper(num):
        import time
        time_first = time.perf_counter() #время перед вызовом функции
        base_result = function(num)
        time_second = time.perf_counter() #время после вызова функции
        print(f"Время выполнения функции: {time_second - time_first:0.10f} сек.")
        return base_result

    return wrapper
    raise NotImplementedError

@time_execution
def factorial(n):  #функция для проверки
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact
print(factorial(25))