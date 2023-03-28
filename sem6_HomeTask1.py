# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

def math_progr(elem, dd, len_len):
    list_list=[]
    for i in range (1, len_len+1):
        list_list.append(elem+(i-1)*dd)
    return list_list


el = int(input('Первый элемент : '))
d = int(input('Разность : '))
el_len = int(input('Количество элемент : '))

math_list = math_progr(el,d,el_len)

print(*math_list, sep=' ')
