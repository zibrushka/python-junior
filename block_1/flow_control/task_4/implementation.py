def get_next_date(some_date):
    """Возвращает следующую дату для заданной

    Args:
        some_date: определенная исходная дата

    Returns: следующая дата
    """
    import datetime
    day_num = some_date.day
    mon_num = some_date.month
    year_num = some_date.year
    mon_31 = [1, 3, 5, 7, 8, 10, 12]
    mon_30 = [4, 6, 9, 11]
    # есть простой способ прибавления 1 дня к дате,
    # однако требуется использовать операторы управления потоком,
    # поэтому выбран такой способ
    if day_num == 30 and mon_num in mon_30:
        day_num = 1
        mon_num += 1
        return datetime.date(year_num, mon_num, day_num)
    elif day_num == 31 and mon_num in mon_31:
        if mon_num == 12:
            year_num += 1
            mon_num = 1
            day_num = 1
            return datetime.date(year_num, mon_num, day_num)
        else:
            day_num = 1
            mon_num += 1
            return datetime.date(year_num, mon_num, day_num)
    elif day_num == 28 and mon_num == 2:
        if (year_num % 4 == 0 and year_num % 100 != 0) or (year_num % 400 != 0):
            day_num += 1
            return datetime.date(year_num, mon_num, day_num)
        else:
            mon_num += 1
            day_num = 1
            return datetime.date(year_num, mon_num, day_num)
    else:
        day_num += 1
        return datetime.date(year_num, mon_num, day_num)
    raise NotImplementedError
