# The zip() function combines elements from two or more iterables into pairs or tuples.
# It matches elements based on their positions and returns a zip object.
# Syntax: zip(iterable1, iterable2, ...)

names = ["Clark", "Alice", "Bob"]
Origin = ["Argentina", "Turkey", "France"]

data = dict(zip(names, Origin))

for key, val in data.items():
    print(f"{key} is from {val}")