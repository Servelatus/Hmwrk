# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_parameters(name, second_name, year, city, email, phone_number):
    return name + ' ' + second_name + ' ' + year + ' года рождения, ' + 'проживает в городе ' \
            + city + ', e-mail: ' + email + ', номер телефона: ' + phone_number

def run():
    print(user_parameters(name='Вася', second_name='Пупкин', year='1974', city='Бухалово' \
        , email='vasya@pupkin.ru', phone_number='999-777-55-33-11'))

run()