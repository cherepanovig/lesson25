# Домашнее задание по теме "Зачем нужно наследование"
# Задача "Съедобное, несъедобное"

class Animal:
    alive = True  # (живой)
    fed = False  # (накормленный)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name}'


class Plant:
    edible = False  # (съедобность)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name}'


class Mammal(Animal):

    def eat(self, food):
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Predator(Animal):

    def eat(self, food):
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Flower(Plant):
    edible = False


class Fruit(Plant):
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
