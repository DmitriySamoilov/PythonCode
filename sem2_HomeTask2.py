# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

# Решение циклами

s = int(input("Введите сумму двух натуральных чисел: "))
p = int(input("Введите произведение двух натуральных чисел: "))

for item in range(1, s//2+1):
    if item*(s-item) == p:
        print(item, s-item)
        break
else:
    print('Нет решений')


# Решение циклами2
s = int(input("Введите сумму двух натуральных чисел: "))
p = int(input("Введите произведение двух натуральных чисел: "))
i=1
while i*(s-i) != p:
    i +=1
print(i, s-i)

# Решение формулой
from math import sqrt
sum = int(input("Введите сумму двух натуральных чисел: "))
mult = int(input("Введите произведение двух натуральных чисел: "))
d = sum * sum - 4 * mult
if d<0 : print('Нет решений')
else:
    x1 = (sum - sqrt(d))/2
    x2 = (sum + sqrt(d))/2
    print((x1),(x2), x1+x2, x1*x2)
