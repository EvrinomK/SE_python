class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f'x: {self.x} y: {self.y}'

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise TypeError()

    def __radd__(self, other):
        if isinstance(other, Point):
            if other == 0:
                return self
            else:
                return self.__add__(other)
        else:
            raise TypeError()

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        else:
            raise TypeError()

    def __iadd__(self, other):
        if isinstance(other, Point):
            self.x += other.x
            self.y += other.y
        else:
            raise TypeError()
    
    def __isub__(self, other):
        if isinstance(other, Point):
            self.x -= other.x
            self.y -= other.y
        else:
            raise TypeError()

    def __eq__(self, other: object) -> bool:
        return self.x == other.x and self.y == other.y

point1 = Point(1, 2)
print(f'Point1: {point1}')
point2 = Point(3, 4)
print(f'Point2: {point2}')

point1.x = 10
point1.y = 11
print(f'Changed Point1: {point1}')
print(f'Sum Point1 and Point2: {point1 + point2}')
print(f'Sum Point2 and Point1: {point2 + point1}')
print(f'Sub Point2 from Point1: {point1 - point2}')
print(f'Sub Point1 from Point2: {point2 - point1}')
print(f'Eq Point1 with Point2: {point2 == point1}')
print(f'Eq Point1 with Point1: {point1 == point1}')
print(f'Eq Point2 with Point2: {point2 == point2}')