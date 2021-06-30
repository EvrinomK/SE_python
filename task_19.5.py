class Animal:
    name = ''

    def __init__(self) -> None:
        print('Родилось животное')

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def eat(self):
        print(f'{self.name} жреть. Ням ням.')

    def makeNoise(self):
        print(f'{self.name} говорит гррр')

class Cat(Animal):

    def __init__(self) -> None:
        Animal.__init__(self)
        print('Родилося котэ')

    def makeNoise(self):
        print(f'{self.name} говорит Мяу')

class Dog(Animal):

    def __init__(self) -> None:
        Animal.__init__(self)
        print('Родилась собака')

    def makeNoise(self):
        print(f'{self.name} говорит Гав')

    
def speak(obj: Animal):
    obj.makeNoise()
    obj.eat()

cat = Cat()
my_favourite_dog = Dog()
my_dog = Dog()
scorpion = Animal()

cat.setName('Петр Михалыч')
my_dog.setName('Дуроти')
my_favourite_dog.setName('Чакуша')
scorpion.setName('Катя')

speak(cat)
speak(my_dog)
speak(my_favourite_dog)
speak(scorpion)

