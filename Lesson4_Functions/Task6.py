# Задание №6
# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.

def sum_list(numbers: list[int | float], num1: int, num2: int) -> int | float:
    size = len(numbers)
    min_i, max_i = sorted([num1, num2])
    min_i = min_i if min_i > 0 else 0
    max_i = max_i if max_i < size else size
    return sum(numbers[min_i: max_i])

s = [73, 42, 7, 3, 5, 2, 11, 100, 500, 1, -750]

print(sum_list(s, 3, 12))