# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.
import json

def read_file():
    with open('file7.txt', 'r') as f:
        firm = dict()
        list_of_firm = []
        average = 0
        for line in f:   #расчитываем прибыль для каждой фирмы
             firm_info = line.split()
             firm[firm_info[0]] = int(firm_info[2]) - int(firm_info[3])
        for key in firm:
             average += firm[key]

        firm['average_profit'] = average / len(firm)
    list_of_firm.append(firm)

    return list_of_firm


def to_json(list):
    with open('data.json', 'w+') as j_f:
        print('ого ',list)
        list = json.dump( list,j_f)
        print('Итого ', list)
def run():
    to_json(read_file())

run()