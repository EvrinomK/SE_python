from math import sqrt, sin, pi
import doctest 

def calculate_z(x, y):
    return (x + (2 + y)/x**2)/(y + 1/sqrt(x**2 + 10))

def calculate_q(x, y):
    """
    >>> calculate_q (0, 0)
    0.0

    >>> calculate_q (0, 1.0)
    1.0

    """
    return 2.8 * sin(x) + abs(y)

doctest.testmod()

x = float(input('Введите x: '))
y = float(input('Введите y: '))

print(f'z = {calculate_z(x, y)}')
print(f'q = {calculate_q(x, y)}')

