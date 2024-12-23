"""Сортировка по шаблону.

По прибытии на Марс грузового космического корабля робот-грузчик должен 
расставить прибывшие контейнеры в определённом порядке. Контейнеры
пронумерованы вразнобой, а номера могут повторяться. Нумерация может быть,
например, такой:

# Прибыло 11 контейнеров:
2 3 1 3 2 4 6 7 9 2 19
У робота-грузчика есть инструкция, шаблон, в котором указано, в каком порядке
должны стоять контейнеры:
2 1 4 3 9 6
Из этой инструкции следует, что сперва должны стоять все контейнеры с номером 2
(сколько бы их ни было на борту), следом — все контейнеры с номером 1,
дальше — все контейнеры с номером 4 — и так до конца шаблона-инструкции.

Если же в грузовике окажутся контейнеры, не учтённые в инструкции, их надо 
поставить последними, в порядке возрастания.

2 3 1 3 2 4 6 7 9 2 19  # Номера контейнеров в грузовике.

2 1 4 3 9 6  # Шаблон-инструкция

2 2 2 1 4 3 3 9 6 7 19  # Результат работы робота-грузчика.

# Контейнеры 7 и 19 не были упомянуты в инструкции. 
# Они переставлены в конец результирующего массива 
# и отсортированы от меньшего к большему.
# И это правильно, так и надо.
Ваша задача — написать программу, которая:

будет принимать на вход массив для сортировки и массив-шаблон,
в соответствии с которым должна быть выполнена сортировка;
вернёт массив, отсортированный в соответствии с шаблоном.

Формат ввода
В первой строке передаётся количество чисел, которые нужно отсортировать, n.
Оно не превосходит 1500.

Во второй строке передаются n чисел, которые надо отсортировать.
Значения этих чисел не превосходят 1000.

В третьей строке передаётся длина массива-шаблона m. Длина массива 
не превосходит 1500.

В четвёртой строке передаётся массив-шаблон, в соответствии с которым нужно
отсортировать первый массив. Значения в этом массиве не превосходят 1000.

В первом массиве гарантированно присутствуют все числа из массива-шаблона.

Формат вывода
Выведите в строку через пробел значения из первого массива, отсортированные 
в соответствии с шаблоном.
"""

from typing import List


def sort_by_template(unsorted_arr: List[int], template: list[int]) -> str:
    """Сортирует массив по шаблону."""
    result = ''
    remains = []
    for el in template:
        for num in unsorted_arr:
            if num == el:
                result += str(num) + ' '
                # unsorted_arr.remove(num)
    for num in unsorted_arr:
        if num not in template:
            remains.append(num)

    if remains:
        remains.sort()
        for num in remains:
            result += str(num) + ' '

    return result.rstrip()


if __name__ == '__main__':
    array_size = int(input())
    unsorted_arr = [int(i) for i in input().split()]
    template_size = int(input())
    template = [int(i) for i in input().split()]

    print(sort_by_template(unsorted_arr, template))

    # test_1_1 = [2, 4, 3, 5, 6, 0, 9, 8, 7, 7]
    # test_1_2 = [2, 4, 3, 5, 6, 0]

    # test_2_1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    # test_2_2 = [2, 1, 4, 3, 9, 6]

    # test_3_1 = [3, 10, 5, 9, 2, 7, 6, 0, 8, 3, 4]
    # test_3_2 = [3, 10, 5, 9, 2, 7, 6, 0]

    # assert sort_by_template(test_1_1, test_1_2) == '2 4 3 5 6 0 7 7 8 9'
    # assert sort_by_template(test_2_1, test_2_2) == '2 2 2 1 4 3 3 9 6 7 19'
    # assert sort_by_template(test_3_1, test_3_2) == '3 3 10 5 9 2 7 6 0 4 8'