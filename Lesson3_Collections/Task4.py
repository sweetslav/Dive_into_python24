# Задание №4
# Погружение в Python | Коллекции
# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

#1
data = [42, 73, 5, 42, 42, 2, 3, 5, 7, 73, 42]

element_count = {}
for item in data:
    if item in element_count:
        element_count[item] += 1
    else:
        element_count[item] = 1

for item, count in element_count.items():
    if count == 2:
        data = [x for x in data if x != item]

print(data)


#2
data = [42, 73, 5, 42, 42, 2, 3, 5, 7, 73, 42]

unique_list = [item for item in data if data.count(item) != 2]

print(unique_list)

#3
data2 = [42, 73, 5, 42, 42, 2, 3, 5, 7, 73, 42]
COUNT = 2

for item in set(data2):
    if data.count(item) == COUNT:
        for _ in range(COUNT):
            data2.remove(item)
print(data2)