class Organism:

    alive = True

    def type(self):
        print(f'The type is mammal')

class Animal(Organism):

    type = 'Reptile'

class Alligator(Animal):

    def type(self):
        print(f'The type is {Animal.type}')


alligator = Alligator()

alligator.type()