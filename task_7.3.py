def define_parity(value):
    return value % 2 == 0

value = float(input('Введите число: '))
print(f'Число {value} является { "четным" if define_parity(value) else "нечетным"}')