# Задача 2: Найдите сумму цифр трехзначного числа. 
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

#Без циклов и условий

#Первый вариант как строка
x =input("Введите трехзначное число:")
print(f'Сумма цифр {x} равна {int(x[0])+int(x[1])+int(x[2])} ({x[0]} + {x[1]} + {x[2]})')

#Второй вариант как число

x =int(input("Введите трехзначное число:"))
print(f'Сумма цифр {x} равна {x%10+x//10%10+x//100} ({x//100} + {x//10%10} + {x%10})')

#Третий вариант - число произвольного размера

x =input("Введите целое число:")

x_list=[int(item) for item in x]

print(f'Сумма цифр {x} равна {sum(x_list)} = ', *x_list, sep = " + " )
