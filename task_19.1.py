
class Cat:
    name = ''
    color = ''
    weight = ''

    def __init__ (self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def meow(self):
        print(f'Котэ по имени {self.name} цвета {self.color} весом в {self.weight} сказало мяу!')

not_my_cat = Cat('Зло во влоти', 'черного словно смоль', 'центнер')
not_my_cat.meow()