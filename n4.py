# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
number = int(input('Введите число: '))
max = 0
while number > 1:
    x = number % 10
    if max < x:
        max = x
    number //= 10
print(max)

# max_number = 0
# n = input('Введите число ')
# for i in range(len(n)):
#     if max_number < int(n[i]): max_number = int(n[i])
# print('Max = ', max_number)
