# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Store:

    def __init__(self, name, volume):
        self.name = name
        self.volume = volume
        self.unit = {'printer':0, 'scanner':0, 'copier':0}

    def __str__(self):
        print(f'Помещение {self.name}, свободно {self.volume}, {self.unit}')
        return ''
    def __add__(self, other):
        if self.volume - other.volume < 0:
            print('Склад переполнен!')
        else:
            self.volume = self.volume - other.volume
            self.unit[other.name] = self.unit[other.name] + 1

    def mul(self, other, quantity):
        try:
            quantity = int(quantity)
            if self.volume - (other.volume * quantity) < 0:
                print('Склад переполнен!')
            else:
                self.volume = self.volume - (other.volume * quantity)
                self.unit[other.name] = self.unit[other.name] + quantity
        except ValueError:
            print('Странное какое-то количество...')

    def move(self, other, equipment):
        self.volume = self.volume - equipment.volume
        other.volume = other.volume + equipment.volume
        self.unit[equipment.name] = self.unit[equipment.name] - 1
        other.unit[equipment.name] = other.unit[equipment.name] + 1

class OfficeEquipment:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume



class Printer(OfficeEquipment):
    def __init__(self):
        self.name = 'printer'
        self.volume = 5

    def purpose(self):
        print('Печать')

class Scanner(OfficeEquipment):
    def __init__(self):
       self.name = 'scanner'
       self.volume = 1

    def purpose(self):
        print('Сканирует')

class Copier(OfficeEquipment):
    def __init__(self):
        self.name = 'copier'
        self.volume = 20

    def purpose(self):
        print('Копирует')


sclad = Store('Склад №1', 150)
office = Store('Офис', 30)

hp = Printer()
iScan = Scanner()
cannon = Copier()

sclad + hp #добавляем принтер на склад
sclad.mul(hp, 5)
sclad.mul(iScan, 5)
sclad.mul(cannon, 2)
print(sclad)
sclad.move(office, cannon) #перевозим копир со склада в офис
print(sclad)
print(office)
unit = input('что будем добавлять на склад? (1 - принтер, 2 - сканер, 3 - копир) ')
number = input('введите количество ')
if unit == '1':
    sclad.mul(hp, number)
elif unit == '2':
    sclad.mul(iScan, number)
elif unit == '3':
    sclad.mul(cannon, number)
else:
    print('Такой техники у нас нет...')


