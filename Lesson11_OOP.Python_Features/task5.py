# Задание №5
# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длину и ширину.
# При вычитании не допускайте отрицательных значений.

class Rectangle:
    def __init__(self, width, length=None):
        self.width = width
        if length:
            self.length = length
        else:
            self.length = width

    def perimeter(self):
        return 2 * self.width + 2 * self.length

    def area(self):
        return self.length * self.width

    def __add__(self, other):
        perimeter = self.perimeter() + other.perimeter()
        length = self.length + other.length
        width = perimeter / 2 - length
        return Rectangle(width, length)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        perimeter = self.perimeter() - other.perimeter()
        length = abs(self.length - other.length)
        width = abs(perimeter / 2 - length)
        return Rectangle(width, length)

    def __str__(self):
        return f' Длина прямоугольника = {self.length}, ширина прямоугольника = {self.width}'


if __name__ == '__main__':
    rectangle_1 = Rectangle(3, 5)
    print(rectangle_1.area())
    rectangle_2 = Rectangle(4, 2)
    print(rectangle_1.perimeter())
    print(rectangle_2.perimeter())
    print(rectangle_1 + rectangle_2)
    print(rectangle_1 - rectangle_2)
