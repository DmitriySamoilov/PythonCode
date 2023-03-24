# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def Multipal_rec(m , n):
    if n==0 : return 1
    return m * Multipal_rec ( m, n-1)


def main():
    
    print(Multipal_rec(int(input()),int(input())))


if __name__ == '__main__':
    main()