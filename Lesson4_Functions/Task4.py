# Задание №4
# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.
from timeit import timeit


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


data_list = [73, 42, 7, 3, 5, 2, 11]
print('Исходный список: ', data_list)
bubble_sort(data_list)
print('Отсортированный список: ', sorted_list)
print(timeit('bubble_sort(data_list)', globals=globals()))
