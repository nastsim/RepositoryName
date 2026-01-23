# TODO Напишите функцию для поиска индекса товара
def find_item_index(items_list, item_to_find):
    # Проходим по всем элементам списка
    for index, item in enumerate(items_list):
        # Если нашли искомый товар
        if item == item_to_find:
            return index  # Возвращаем индекс первого вхождения

    # Если товар не найден
    return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")