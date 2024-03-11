# Задание №7
# Погружение в Python | Коллекции
# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают или не совпадают в ваших решениях.

#1
text = input("Enter a text: ")
result = {}

for char in set(text):
    result[char] = text.count(char)
print(result)


#2
text2 = input("Enter a text: ")
result2 = {}

for char in text2:
    if char not in result2:
        result2[char] = 1
    else:
        result2[char] += 1

print(result2)

#3
text3 = input("Enter a text: ")
result3 = {}

for char in text3:
    result3[char] = result3.get(char, 0) + 1

print(result3)