# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

#Без циклов

#Первое решение как строка

x=input("Номер билета (6 цифр) :")

flag =int(x[0])+int(x[1])+int(x[2])==int(x[3])+int(x[4])+int(x[5])

print("Yes" if flag else "No")

#Второе решение как число

x=int(input("Номер билета (6 цифр) :"))

flag =x//100000+x//10000%10+x//1000%10==x%10+x//10%10+x//100%10

print("Yes" if flag else "No")