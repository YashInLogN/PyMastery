# Dictionary comprehension is a short and simple way to create a dictionary.
# It allows you to generate key-value pairs using a loop and an optional condition.
# Syntax: {key: value for item in iterable if condition}

cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

cities_f_sorted = dict(sorted(cities_in_F.items(), key= lambda item: item[1]))

print(cities_f_sorted)