class Animal:

    alive = True

    def __init__(self, name, type):
          self.name = name
          self.type = type

    def eat(self):
          print(f"{self.name} is eating.")

    def sleep(self):
          print(f"{self.name} is sleeping.")


    def hungry(self):
          print(f"{self.name} is hungry")

class Rabbit(Animal):
      def run(self):
            print(f'{self.name} is running.')
class Fish(Animal):
      def swim(self):
            print(f'{self.name} is swimming.')
class Hawk(Animal):
      def fly(self):
            print(f'{self.name} is flying.')