# Задание №3
# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.

def get_unicode_dict(text: str) -> dict[str, int]:
    num1, num2 = map(int, text.split())
    result = {}
    for num in range(min(num1, num2), max(num1, num2) + 1):
        result[chr(num)] = num
        #result.setdefault(chr(num), num)

    return result


print(get_unicode_dict('61 94'))
