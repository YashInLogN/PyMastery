# List comprehension is a short and simple way to create a new list.
# It combines a loop and an optional condition in a single line.
# Syntax: [expression for item in iterable if condition]

import random
create = random

# squared_list = list((lambda: x**2)() for x in range(1, 11))
# squared_list_ = [x * x for x in range(1, 11)]

grades_list = list(create.randrange(10, 100, 15) for _ in range(10))
# grades_list_sorted = list(filter(lambda x: x > 50, grades_list))
grades_list_sorted = [i for i in grades_list if i > 50]

grades_list_handled = [i if i > 50 else "Failed" for i in grades_list]

print(grades_list)
print(grades_list_handled)
