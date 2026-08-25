# The map() function applies a given function to every item in an iterable.
# It returns a map object containing the results.
# It is commonly used with lambda functions for quick transformations.

# map(function, iterable)

store = [("shirt",20.00),
        ("'pants",25.00),
        ("jacket",50.00),
        ("socks", 10.00)]

to_euros = lambda data: (data[0], data[1]*0.82)

store_euros = tuple(map(to_euros, store))

for i in store_euros:
    print(i)



