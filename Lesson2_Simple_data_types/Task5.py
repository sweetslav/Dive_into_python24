# Задание №5
# напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
# Используйте комплексные числа для извлечения квадратного корня.

a = float(input("Enter an A coefficient : "))
b = float(input("Enter a B coefficient : "))
c = float(input("Enter a C coefficient : "))
result = ''
d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b + pow(d, 0.5)) / (2 * a)
    x2 = (-b - pow(d, 0.5)) / (2 * a)
    result = f'The equation has two solutions: {x1 =}, {x2 =}'
elif d == 0:
    x1 = (-b - pow(d, 0.5)) / (2 * a)
    result = f'The equation has one solution: {x1 =}'
else:
    d = complex(d, 0)
    x1 = (-b + pow(d, 0.5)) / (2 * a)
    x2 = (-b - pow(d, 0.5)) / (2 * a)
    result = f'The equation has two solutions: {x1 =}, {x2 =}'

print(result)