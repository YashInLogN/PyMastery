# Dictionary comprehension is a short and simple way to create a dictionary.
# It allows you to generate key-value pairs using a loop and an optional condition.
# Syntax: {key: value for item in iterable if condition}

cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
print(f"Cities and temperatures(F)--->\n{cities_in_F}")
# cities_F_sorted = dict(sorted(cities_in_F.items(), key= lambda item: item[1]))
# print(cities_F_sorted)

print('\n')

cities_in_C = {key: ((value-32)*(5/9)) for (key, value) in cities_in_F.items()}
print(f"Cities and temperatures(C)--->\n{cities_in_F}")

# cities_weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}
# check_cities_weather = {key: "Successfully" for (key,value) in cities_weather.items() if value=="snowing"}
# print(check_cities_weather)

def check_temp(v):
    if v > 70:
        return "HOT"
    elif 50 <= v < 70:
        return "WARM"
    else:
        return "COLD"

# filter_temperature = {key: ("WARM" if value > 50 else "COLD") for (key, value) in cities_in_F.items()}
filter_temperature = {key: check_temp(value) for (key, value) in cities_in_F.items()}

print(filter_temperature)