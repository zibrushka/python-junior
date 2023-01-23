def get_numbers():
    """Возвращает все числа от 1000 до 2000, которые делятся на 7, но не кратны 5
    Returns: итерируемый объект с нужными числами
    """
    numbers = []
    for i in range(1000, 2000):
        k = i % 7
        y = i % 5
        if k == 0:
            if y != 0:
                numbers.append(i)
    return numbers
    raise NotImplementedError
