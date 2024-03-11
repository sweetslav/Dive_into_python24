# Задание №3
# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итератор.
# ✔ Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.

COUNT = 5

text = input('Enter a string: ')

result = {char: ord(char) for char in text}
print(f'{text = }')

dict_iter = iter(result.items())

for _ in range(COUNT):
    print(*next(dict_iter))