class Organism:

    alive = True

    def __init__(self, name):
        self.name = name

class Animal(Organism):

    def eat(self):
        print(f'{self.name} is eating.')

class Cat(Animal):

    def hobby(self):
        print(f'{self.name} is resting.')

cat = Cat('Liza')

print(cat.alive)

cat.eat()
cat.hobby()