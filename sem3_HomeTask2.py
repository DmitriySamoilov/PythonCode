# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
# 5
# 1 2 3 4 5
# 6    -> 5


import random


def number_search(list, item):
    m = abs(list[0] - item)
    mi = 0
    i = 1
    while i < len(list):
        if abs(list[i] - item) == 0:
            return (list[i], i)
        if abs(list[i] - item) < m:
            m = abs(list[i]-item)
            mi = i
        i += 1
    return (list[mi], mi)


def main():
    n = int(input("Введите размер списка: "))
    list_source = [random.randint(1, n) for i in range(1, n+1)]
    print(list_source)
    print(
        f'Ближайшее число {number_search(list_source,int(input("Введите число для поиска: ")))}')


if __name__ == '__main__':
    main()
