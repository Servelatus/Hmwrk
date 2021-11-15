# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:

    def __init__(self, title):

        self.title = title

    def draw(self):

        print('Запуск отрисовки.')

class Pen(Stationery):

    def draw(self):
        print('Сняли колпачок, начали писать')

class Pencil(Stationery):

    def draw(self):
        print('Карандаш скрипит по бумаге')

class Marker(Stationery):

    def draw(self):
        print('Маркер начал марать бумагу')


big = Pen('Big')
big.draw()

karandash = Pencil('Огрызок')
karandash.draw()

marker_blue = Marker('Синий')
marker_blue.draw()


