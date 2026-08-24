# The sort() function is used to arrange the elements of a list in ascending order.
# It can also sort elements in descending order using the reverse=True argument.
# sort() changes the original list directly.

students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr .Krabs"]

students.sort(reverse=True)

for i in students:
    print(i)