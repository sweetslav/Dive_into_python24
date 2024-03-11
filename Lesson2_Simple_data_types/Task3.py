# Задание №3
# ✔ Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# ✔ избегайте магических чисел
# ✔ добавьте аннотацию типов, где это возможно

BIN = 2
OCT = 8

number: int = int(input("Enter a number:"))

for div in BIN, OCT:
    test_number: int = number
    result: str = ''
    while test_number:
        current_digit = test_number % div
        result = str(current_digit) + result
        test_number //= div
    print(f'For {div} result is {result}')