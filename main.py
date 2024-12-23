def calculate_mean(values):
    """
    Рассчитывает среднее арифметическое списка чисел.

    Args:
        values (list of float): Список чисел для расчёта.

    Returns:
        float: Среднее арифметическое значений.

    Raises:
        ValueError: Если список пустой.
    """
    if not values:
        raise ValueError("Список не должен быть пустым")
    return sum(values) / len(values)
