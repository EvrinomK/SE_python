from functools import reduce

values = []
values.append(int(input('Введите первое число: ')))
values.append(int(input('Введите второе число: ')))
values.append(int(input('Введите третье число: ')))

print(f'Сумма введенных чисел: {sum(values)}')
print(f'Произведение введенных чисел: {reduce(lambda lvalue, rvalue: lvalue*rvalue, values, 1)}')
