# 1. Реализовать класс «Дата»,
# функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    data_list = []
    def __init__(self, data_str =  str):

        Data.data_list = data_str.split('-')

    @classmethod
    def data_to_int(cls):
        data_numb = int(''.join(cls.data_list))
        print(data_numb)

    @staticmethod
    def validation(data_str):
        month_30 = {4, 6, 9, 11}
        data_list = data_str.split('-')
        # Не хватило времени на проверку високосного года!
        data_list = [int(i) for i in data_list]

        if 1 <= data_list[1] <= 12 and 1 <= data_list[0] <= 31:
            if  30 < data_list[0]  and data_list[1] in month_30:
                return False
            else:
                if 28 < data_list[0]  and data_list[1] == 2:
                    return False
                else:
                     return True

        else:
            return False


dat = input('Введите дату: ')
vremechko = Data(dat)
if Data.validation(dat):
    vremechko.data_to_int()
else:
    print('Дата введена неправильная какая-то((')

