# Задание №4
# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых значений (отрицательных).
# Используйте декораторы свойств.

class Rectangle:
    def __init__(self, width, length=None):
        self._width = width
        if length:
            self._length = length
        else:
            self._length = width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError('Width must be greater than 0')

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value > 0:
            self._length = value
        else:
            raise ValueError('Length must be greater than 0')


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
    rectangle_1 = Rectangle(3, 6)
    rectangle_2 = Rectangle(5, 3)
    #rectangle_1.width = -3
    print(rectangle_1 - rectangle_2)


