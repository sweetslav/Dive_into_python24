# Создайте в переменной data список значений разных типов перечислив их через
# запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# ✔ порядковый номер начиная с единицы
# ✔ значение
# ✔ адрес в памяти
# ✔ размер в памяти
# ✔ хэш объекта
# ✔ результат проверки на целое число только если он положительный
# ✔ результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.
import sys
data = [42, 73.0, 'Hello World!', True, 42, 256, 2 ** 7, 1, 'Hello World!']

for n, item in enumerate(data, 1):
    check_int = 'Число является целым' if isinstance(item, int) else ''
    check_str = 'Это строка' if isinstance(item, str) else ''
    print(f'{n}. Object {item}\nAdress: {id(item)};\tSize: {sys.getsizeof(item)};\t'
          f'Hash: {hash(item)};\t{check_int}{check_str}\n')