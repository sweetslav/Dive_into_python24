# Задание №2
# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.

from collections import deque
import json
import time
from pathlib import Path


class Factorial:

    def __init__(self, k):
        self.memory = deque(maxlen=k)

    def __call__(self, n, *args, **kwargs):
        res = 1
        for num in range(2, n + 1):
            res *= num
        self.memory.append({n: res})

        return self.memory[-1]

    def old(self):
        return self.memory

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        dump_dict = {}
        while self.memory:
            dump_dict.update(self.memory.popleft())
        with open(f'{int(time.time())}.json', 'w', encoding='utf-8') as f:
            json.dump(dump_dict, f)


if __name__ == '__main__':
    fact = Factorial(5)
    for i in range(2, 20, 2):
        print(fact(i))
        print(fact.old())

    with fact as fd:
        fd(5)
