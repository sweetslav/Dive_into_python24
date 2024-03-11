# Задание №5
# Доработаем прямоугольник и добавим экономию памяти
# для хранения свойств экземпляра без словаря __dict__.

class Rectangle:
    __slots__ = ('_width', '_length')

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
    rectangle = Rectangle(4, 8)
    print(Rectangle.__dict__)