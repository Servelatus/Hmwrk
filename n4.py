# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, name, speed, color,  is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')


    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):

        print(f'{self.name} едет со скоростью { self.speed}')



class TownCar(Car):

    def show_speed(self):
        if self.speed > 60: print(f'{self.name} превышает скорость')
        else: print(f'{self.name} едет со скоростью {self.speed}')


class SportCar(Car):
    pass



class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} превышает скорость')
        else:
            print(f'{self.name} едет со скоростью {self.speed}')
class PoliceCar(Car):
    def siren(self):
        print('Сирена включена!')

lada = TownCar('Жигули', 50, "red", False)
lamba = SportCar('Ламборгини', 250, "yllow", False)
garbage_truck = WorkCar('Мусоровоз', 50, "black", False)
musorovoz = PoliceCar('Полиция', 50, "white", True)

lada.go()
lada.show_speed()
lada.turn('Направо')
lada.stop()


lamba.go()
lamba.show_speed()

garbage_truck.go()
garbage_truck.show_speed()

musorovoz.go()
musorovoz.show_speed()
musorovoz.siren()
print('цвет ',musorovoz.color)

