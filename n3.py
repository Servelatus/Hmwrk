# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней
# величины дохода сотрудников.

def read_file():
    with open('file3.txt', 'r') as f:
        wage_list = f.read()
        print(wage_list)
        wage_list = wage_list.split()
    return wage_list

def minimum_wage(wage_list):
    print('Зарплата меньше 20тыс у:')
    for i, wage in enumerate(wage_list):
        if wage.isdigit():
            if int(wage) < 20000:
                print(wage_list[i - 1])

def average_wage(wage_list):
    average = 0
    for i in range(1,len(wage_list),2):
        average += int(wage_list[i])

    print('Средняя зарплата: ', average / (len(wage_list) / 2))




def run():
    wage_list = read_file()
    minimum_wage(wage_list)
    average_wage(wage_list)


run()