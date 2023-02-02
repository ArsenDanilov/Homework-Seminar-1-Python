import math

x1 = int(input('Введите координату по оси X для A: '))
y1 = int(input('Введите координату по оси Y для A: '))
x2 = int(input('Введите координату по оси X для B: '))
y2 = int(input('Введите координату по оси Y для B: '))

distance = round(((math.sqrt((x2 - x1)**2 + (y2 - y1)**2))),2)
print(f'Расстояние от точки A до точки B в 2D пространстве равняется {distance}')