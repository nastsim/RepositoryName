# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, separator=","):
    # Разделяем строки на списки участников
    participants1 = group1.split(separator)
    participants2 = group2.split(separator)

    # Преобразуем в множества для нахождения пересечения
    set1 = set(participants1)
    set2 = set(participants2)

    # Находим общих участников
    common_participants = set1.intersection(set2)

    # Преобразуем в список и сортируем в алфавитном порядке
    sorted_common = sorted(list(common_participants))

    return sorted_common


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
result = find_common_participants(
    participants_first_group,
    participants_second_group,
    separator="|"
)

print(f"Общие участники: {result}")