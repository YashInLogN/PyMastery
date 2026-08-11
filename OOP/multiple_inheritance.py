class Prey:

    def prey(self):
        print(f'This animal flees.')

class Predator:

    def hunt(self):
        print(f'This animal is hunting.')

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.prey()
hawk.hunt()
