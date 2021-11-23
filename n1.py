# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
# первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, a, b, x =  list()):

        self.x = x
        self.a = a
        self.b = b

    def __str__(self):
        for xx in self.x:
            for yy in xx:
                print (f'{yy:02}', end = ' ')
            print('\n')

        return  ''


    def __add__(self, other):
        sum_matrix = []
        for i in range(self.a):
            sum_matrix.append([])
            for k in range(self.b):
                sum_matrix[i].append(0)

        for row in range(self.a):
            for el in range(self.b):
               sum_matrix[row][el] = self.x[row][el] + other.x[row][el]
        return Matrix(self.a, self.b, sum_matrix)



matrix1 = Matrix(3, 4, [[1, 2, 3, 4],[11, 12, 13, 14], [21, 22, 23, 24]])
matrix2 = Matrix(3, 4, [[1, 1, 1, 1],[1, 1, 1, 1], [1, 1, 1, 1]])

print(matrix1, matrix2)
super_matrix = matrix1 + matrix2
print(super_matrix)


