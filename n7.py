# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b)

    def __str__(self):
        if self.b == 1:
            b = ''
        else: b = self.b
        return f'{self.a} + {b}i'

Cmplx1 = Complex(2, -3)
Cmplx2 = Complex(-5, 4)
print(Cmplx1 + Cmplx2)
print(Cmplx1 * Cmplx2)
