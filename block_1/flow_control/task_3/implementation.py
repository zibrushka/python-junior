def get_days_count_by_month(month):
    """Возвращает количество дней по месяцу

    Args:
        month: название месяца

    Returns: количество дней
    """
    from datetime import datetime
    from calendar import monthrange

    name_month = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    current_year = datetime.now().year
    if month in name_month:
        return monthrange(current_year, name_month.index(month)+1)[1] #нумерация индексов в списке идет с 0, поэтому к индексу прибавим 1
    else:
        return 0
    raise NotImplementedError