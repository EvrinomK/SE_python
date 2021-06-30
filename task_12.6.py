summ = 0
while True:
    line = input('Введите значение: ')
    if line == 'стоп':
        break
    else:
        summ += float(line)
print(summ)