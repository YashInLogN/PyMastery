class Car:

    color = None

class Truck:

    color = None

def change_color(car, color):
    car.color = color

car1 = Car()
car2 = Car()
car3 = Car()

truck1 = Truck()
truck2 = Truck()

change_color(car1, 'Grey')
change_color(car1, 'Green')
change_color(car1, 'Black')

change_color(truck1, "White")
change_color(truck2, "Red")
# car1.color = 'Grey'
# car2.color = 'Green'
# car3.color = 'Black'

print(car1.color)
print(truck2.color)