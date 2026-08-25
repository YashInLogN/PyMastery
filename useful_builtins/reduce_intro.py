# The reduce() function applies a function cumulatively to the elements of an iterable.
# It reduces the entire iterable to a single final value.
# Parameters required: reduce(function, iterable)
# It is available in Python through the functools module.

import functools

# def add(x, y):
#     return x+y

cumulatively = functools.reduce

letters = ["H", "E", "L", "L", "O"]

word = cumulatively(lambda x, y :x+y, letters)

print(word)

factorial = list(range(1, 6))

factorial_ = cumulatively(lambda x, y: x*y, factorial)

print(factorial_)

