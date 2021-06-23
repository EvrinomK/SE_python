L = [3, 6, 7, 4, -5, 4, 3, -1] 

sum_l =  sum(L)

if sum_l > 2:
    print(len(L))

if abs(min(L) - max(L)) > 10:
    print(sorted(L))
else:
    print('Разность меньше 10')