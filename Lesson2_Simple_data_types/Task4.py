# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.

import math
import decimal

decimal.getcontext().prec = 50
PI = decimal.Decimal(math.pi)

diametr = decimal.Decimal(input('Enter the diameter of the circle: '))

while diametr > 1000:
    print('Your number is out of range')
    diametr = decimal.Decimal(input('Enter the diameter of the circle: '))

square = PI * pow(diametr / 2, 2)
length = PI * diametr
print(f'The area of the circle is {square}')
print(f'The length of the circle is {length}')