# Задание №2
# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.

class Rectangle:
    def __init__(self, width, length=None):
        self.width = width
        if length:
            self.length = length
        else:
            self.length = width

    def get_area(self):
        return self.width * self.length

    def get_perimeter(self):
        return (self.width + self.length) * 2



if __name__ == '__main__':
    area_1 = Rectangle(4, 8)
    print(area_1.get_area())
    print(area_1.get_perimeter())
