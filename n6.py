# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента —
# номер товара и словарь с параметрами  (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
#
# (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
# (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
# (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
#
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
#
# 'название': ['компьютер', 'принтер', 'сканер'],
# 'цена': [20000, 6000, 2000],
# 'количество': [5, 2, 7],
# 'ед': ['шт.']

details = ('название', 'цена', 'количество', 'ед')

product_list = []
product = []
product_details = []
for n in range(int(input('количество товаров? '))):
    for i in details:
        product_details.append(input(f'введите {i}: '))

    product = (n+1, dict(zip(details, product_details)))
    product_list.append(tuple(product))
    product_details.clear()

print('Итого 1: ',product_list)

dictinary = {}
trans_dic = {}
for l in product_list:    #извлекаем кортеж из списка
    trans_dic = l[1]  #достаём словарь из кортежа

    for key, value in trans_dic.items():
        dictinary.setdefault(key, []).append(value) #заполняем новый словарь


print('Итого 2: ', dictinary)
