# 3. Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        print(self.name + ' ' + self.surname)


    def get_total_income(self):
        z = self._income.get('wage') + self._income.get('bonus')
        print(f'{self.position} получает {z} рублей')

unit_one = Position('Вася', 'Иванов', 'менеджер', 200, 50)
unit_two = Position('Витя', 'Цой', 'музыкант', 100, 10)

unit_one.get_full_name()
unit_two.get_full_name()

unit_one.get_total_income()
unit_two.get_total_income()
