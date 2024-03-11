# Задание №1
# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.

from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * self.radius * pi

    def area(self):
        return self.radius * self.radius * pi


if __name__ == '__main__':
    circle_1 = Circle(3)
    print(f'{circle_1.perimeter() = }, {circle_1.area() = }')