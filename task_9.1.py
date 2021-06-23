from math import e
from task_9_1_module import calculate_area_by_Gerone, triangle_exists

a = float(input('Введите первую сторону: '))
b = float(input('Введите вторую сторону: '))
c = float(input('Введите третью сторону: '))

if not triangle_exists(a, b ,c):
    print('Треугольник с такими сторонами существовать не может.\nТеорема: Треугольник существует, если каждая его сторона меньше суммы двух других.')
else:
    area = calculate_area_by_Gerone(a, b, c)
    print(f'Площадь: {area}')