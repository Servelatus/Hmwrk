# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randrange

with open('file5.txt', 'w+') as f:
    for i in range(randrange(100)):
        f.write(str(randrange(100)) + ' ')
    f.seek(0)
    number_list = f.read().split()
    sum_value = 0
    for i in number_list:
        sum_value += int(i)
    print(sum_value)
