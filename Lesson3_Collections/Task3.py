# Задание №3
# Погружение в Python | Коллекции
# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

data = (42, 73, 3.14, 'Hello world!', None, True, 'Text', 100500.2, False)

result = {}

for item in data:
    item_type = type(item)
    if item_type not in result:
        result[item_type] = [item]
    else:
        result[item_type].append(item)
print(result)

#2
data = (42, 73, 3.14, 'Hello world!', None, True, 'Text', 100500.2, False)

result = {}

for item in data:
    item_type = type(item)
    if item_type not in result:
        result[item_type] = [el for el in data if type(el) == item_type]

print(result)


#3
data = (42, 73, 3.14, 'Hello world!', None, True, 'Text', 100500.2, False)
result = {}

for item in data:
    key = result.setdefault(type(item), [])
    key.append(item)
print(result)
