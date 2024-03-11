# Задание №3
# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.

import time

class Factorial():
    def __init__(self, *args):
        match len(args):
            case 3:
                self.start, self.stop, self.step = args
            case 2:
                self.start, self.stop = args
                self.step = 1
            case 1:
                self.start = 1
                self.stop = args[0]
                self.step = 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.start < self.stop:
            res = 1
            for num in range(2, self.start + 1):
                res *= num

            self.start += self.step
            return res
        raise StopIteration

if __name__ == '__main__':
    fact = Factorial(15)
    for num in fact:
        print(num, end=' ')
        time.sleep(1)