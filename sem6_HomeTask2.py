# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

list_start =[random.randrange(-10,10) for i in range(10)]
min_max =(-2,5) # заданный диапазон
print (list_start)
list_index = []
for i in range (len(list_start)):
    if min_max[0]<=list_start[i]<=min_max[1]:
        list_index.append(i)
print (list_index)