# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

import random

lst1 = [random.randint(1,20) for item in range (int(input('Введите число: ')))]
lst2 = [random.randint(1,20) for item in range (int(input('Введите число: ')))]
st1 = set(lst1)
st2 = set(lst2)
print(lst1)
print(lst2)
print (st1&st2)