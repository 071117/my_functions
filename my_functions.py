# Тут у меня список полезных функций

# БЫСТРАЯ СОРТИРОВКА УЖЕ ОТСОРТИРОВАННЫХ СПИСКОВ
def quick_merge(n):
    # Создаем список для хранения входных списков
    lists = [input().split() for _ in range(n)]

    # Инициализируем переменную для хранения результата
    merged_result = []

    # Проходим по каждому списку
    for current_list in lists:
        # Указатели для текущего списка и уже объединенного результата
        p1, p2 = 0, 0

        # Временный список для хранения объединенных значений
        temp_result = []

        # Объединяем текущий список с результатом
        while p1 < len(merged_result) and p2 < len(current_list):
            if int(merged_result[p1]) <= int(current_list[p2]):
                temp_result.append(merged_result[p1])
                p1 += 1
            else:
                temp_result.append(current_list[p2])
                p2 += 1

        # Добавляем оставшиеся элементы из merged_result или current_list
        temp_result.extend(merged_result[p1:])
        temp_result.extend(current_list[p2:])

        # Обновляем merged_result для следующей итерации
        merged_result = temp_result

    return merged_result
print('ABOBA')
