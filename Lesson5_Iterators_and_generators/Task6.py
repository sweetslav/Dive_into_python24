# Задание №6
# ✔ Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного генератора, где каждый элемент генератора — отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт» без перехода на новую строку.

LOW_LIMIT = 2
HIGH_LIMIT = 10
COLUMN = 4

table = (
    f'{num_1:>2} * {num_2:>2} = {num_1 * num_2:>2}\t' if num_1 != main_row + COLUMN - 1 else
    f'{num_1:>2} * {num_2:>2} = {num_1 * num_2:>2}\n' if num_2 != HIGH_LIMIT else
    f'{num_1:>2} * {num_2:>2} = {num_1 * num_2:>2}\n\n'
    for main_row in (LOW_LIMIT, LOW_LIMIT + COLUMN)
    for num_2 in range(LOW_LIMIT, HIGH_LIMIT + 1)
    for num_1 in range(main_row, main_row + COLUMN)
)

print(*table)