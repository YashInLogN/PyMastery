from car import Car

car1 = Car('Chevy', 'Corvette', 1990, 'Black')

car2 = Car('Chevy', 'Malibu', 2026, 'Grey')

# Car.wheels = 2
# car1.wheels = 5

car1.drive()

print(car1.wheels)
print(car2.wheels)

car1.drive().stop() # method chaining