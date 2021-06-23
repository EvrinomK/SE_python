from math import sqrt

def triangle_exists(a ,b ,c):
    if a >= b + c or b >= a + c or c >= a + b:
        return False
    else:
        return True

def calculate_area_by_Gerone(a, b ,c):
    half_perimetr = (a + b + c) / 2
    area = sqrt(half_perimetr*(half_perimetr - a)*( half_perimetr - b)*(half_perimetr - c))
    return area