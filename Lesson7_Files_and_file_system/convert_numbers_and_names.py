# Задание №3
# ✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел.
# В новый файл сохраните имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# ✔ При достижении конца более короткого файла, возвращайтесь в его начало.

from pathlib import Path
from typing import TextIO

def read_or_begin(fd: TextIO) -> str:
    """
    Читает следующую строку из файла или перемещает указатель в начало,
    если достигнут конец файла, и читает первую строку.

    Аргументы:
    fd (TextIO): Объект файла для чтения.

    Возвращает:
    str: Прочитанная строка из файла.
    """
    text = fd.readline()
    if not text:
        fd.seek(0)
        text = fd.readline()
    return text.strip()

def convert_data(numbers: str | Path, names: str | Path, result: str | Path) -> None:
    """
    Конвертирует данные из файлов с числами и именами, записывая результат в новый файл.

    Аргументы:
    numbers (str | Path): Путь к файлу с числами.
    names (str | Path): Путь к файлу с именами.
    result (str | Path): Путь к файлу, в который будет записан результат.

    Возвращает:
    None: Функция ничего не возвращает.
    """
    with(
        open(numbers, 'r', encoding='utf-8') as numbers_file,
        open(names, 'r', encoding='utf-8') as names_file,
        open(result, 'w', encoding='utf-8') as result_file
    ):
        len_numbers = sum(1 for _ in numbers_file)
        len_names = sum(1 for _ in names_file)

        for _ in range(max(len_numbers, len_names)):
            nums_str = read_or_begin(numbers_file)
            names_str = read_or_begin(names_file)
            num_int, num_float = nums_str.split('|')
            mult = int(num_int) * float(num_float)
            if mult < 0:
                result_file.write(f'{names_str.lower()} {-mult} \n')
            else:
                result_file.write(f'{names_str.upper()} {int(mult)} \n')


__all__ = ['convert_data']

if __name__ == '__main__':
    convert_data('numbers.txt', 'names.txt', '../Lesson8_Serialization/result.txt')
