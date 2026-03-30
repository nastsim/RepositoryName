import json


def task() -> float:
    """
    Читает JSON файл и вычисляет сумму произведений score * weight
    для каждого словаря в списке.

    Returns:
        Сумма произведений, округленная до 3 знаков после запятой
    """
    FILENAME = "input.json"

    # Читаем JSON файл
    with open(FILENAME, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Вычисляем сумму произведений score * weight
    total_sum = 0.0
    for item in data:
        score = item.get("score", 0.0)
        weight = item.get("weight", 0.0)
        total_sum += score * weight

    # Округляем до 3 знаков после запятой
    return round(total_sum, 3)


if __name__ == '__main__':
    result = task()
    print(result)