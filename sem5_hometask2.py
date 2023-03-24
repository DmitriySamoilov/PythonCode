# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4




def sum_rec(a,b):
    if b==0: return a
    else : return sum_rec(a+1,b-1)


def main():
    
    print(sum_rec(2,2))


if __name__ == '__main__':
    main()