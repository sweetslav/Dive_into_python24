# Задание №4
# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой функции.

from typing import Callable

def counter(num: int):
    def deco(func: Callable):
        def wrapper(*args, **kwargs):
            counters = []
            for count in range(1, num+1):
                print(f'Запуск № {count}')
                res = func(*args, **kwargs)
                counters.append(res)
            return counters
        return wrapper
    return deco

@counter(5)
def summa(a: int, b: int):
    return a + b

if __name__ == '__main__':
    print(summa(2, 3))
