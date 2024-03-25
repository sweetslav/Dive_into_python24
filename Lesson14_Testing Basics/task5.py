# Задание №5
# На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать прямоугольники беря за основу периметр.
# Напишите 3-7 тестов unittest для данного класса.
import unittest

class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.r1 = Rectangle(1, 1)
        self.r2 = Rectangle(10, 20)
        self.r3 = Rectangle(2, 5)
        self.r4 = Rectangle(20, 10)

    def test_create(self):
        self.assertEqual(self.r1, Rectangle(1, 1))

    def test_perimeter(self):
        self.assertEqual(self.r2.perimeter(), 60)

    def test_area(self):
        self.assertEqual(self.r3.area(), 10)

    def test_perimeter_eq(self):
        self.assertEqual(self.r4.perimeter(), self.r2.perimeter())

    def test_area_not_eq(self):
        self.assertNotEqual(self.r1.area(), self.r4.area())

    def test_add(self):
        self.assertEqual(self.r2 + self.r4, Rectangle(30, 30))

    def test_sub(self):
        self.assertEqual(self.r3 - self.r1, Rectangle(1, 4))

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
        if value < 0:
            raise ValueError('Длина прямоугольника должна быть положительной')
        self._width = value

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value < 0:
            raise ValueError('Ширина прямоугольника должна быть положительной')
        self._length = value

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
        width = perimeter / 2 - length
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
    import unittest
    unittest.main()

