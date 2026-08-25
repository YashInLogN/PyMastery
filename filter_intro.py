# The filter() function is used to select elements from an iterable based on a condition.
# It returns a filter object containing only the elements that satisfy the condition.
# Parameters required: filter(function, iterable)
# function → condition to check; iterable → collection of elements to filter.

people = [
    ("Nakul", 18),
    ("Aman", 20),
    ("Rahul", 19),
    ("Priya", 21),
    ("Arjun", 22)
]

check_age = lambda age: age[1] > 18

with_age = list(filter(check_age, people))
age = lambda age: age[1]
sorted_ = sorted(with_age, key=age)

for i in sorted_:
    print(i)

print("Ages after 2 years-----")

age_later = lambda later: (later[0], later[1] + 2)
with_new_age = list(map(age_later, sorted_))

for i in with_new_age:
    print(i)