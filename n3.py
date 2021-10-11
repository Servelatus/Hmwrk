# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    if a < b:
        a, b = b, a
    if b > c:
        max = a + b
    else:
        max = a + c
    return max

def input_arg():
    arg_in = input("Введите через пробел три аргумента: ").split()
    arg =[int(i) for i in arg_in]
    print(my_func(arg[0], arg[1], arg[2]))

def run():
    input_arg()

run()
