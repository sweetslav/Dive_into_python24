# Задание №6
# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.

class Range:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if value < 1:
            raise ValueError('Value must be greater than 0')


class Rectangle:
    width = Range()
    length = Range()

    def __init__(self, width, length=None):
        self.width = width
        self.length = length or width

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

    def __eq__(self, other):
        return self.area() == other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __str__(self):
        return f' Длина прямоугольника = {self.length}, ширина прямоугольника = {self.width}'


if __name__ == '__main__':
    rectangle = Rectangle(-4, 8)
    print(rectangle)
