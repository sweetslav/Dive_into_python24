# Задание №1
# Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и их факториалов.

from collections import deque


class Factorial:

    def __init__(self, k):
        self.memory = deque(maxlen=k)
        # self.memory.append(k)
        # print(self.memory)

    def __call__(self, n, *args, **kwargs):
        res = 1
        for num in range(2, n + 1):
            res *= num
        self.memory.append({n: res})

        return self.memory[-1]

    def old(self):
        return self.memory

if __name__ == '__main__':
    f = Factorial(3)
    for i in range(2, 20, 2):
        print(f(i))
        print(f.old())
