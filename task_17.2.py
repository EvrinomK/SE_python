from random import randint 

def input_natural_number(message):
    try:
        line = input(message)
        result = int(line)

        if float(line) != int(result):
            raise ValueError()

        if result <= 0:
            raise RuntimeError('Значение должно быть больше 0')

        return result
    except ValueError:
        raise RuntimeError('Введенное значение не соответствует типу int')

def input_real_number(message):
    try:
        return float(input(message))
    except ValueError as err:
        raise RuntimeError('Введенное значение не соответствует типу float')

def generate_matrix(lines, columns, l_range, r_range):
    return [[randint(l_range, r_range) for i in range(columns)] for j in range(lines)]

try:
    lines = input_natural_number('Введите кол-во строк матрицы: ')
    columns = input_natural_number('Введите кол-во столбцов матрицы: ')
    l_range = input_real_number('Введите левую границу возможных значений матрицы: ')
    r_range = input_real_number('Введите правую границу возможных значений матрицы: ')

    if l_range >= r_range:
        raise RuntimeError('Левая граница значений должна быть меньше правой границы.')

    matrix = generate_matrix(lines, columns, l_range, r_range)
    print('Сгенерированная матрица:')
    for i in range(len(matrix)):
        print(*matrix[i], sep=' ')

except Exception as err:
    print('Ошибка:')
    print(err)