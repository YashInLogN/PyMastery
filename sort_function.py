# The sort() function is used to arrange the elements of a list in ascending order.
# It can also sort elements in descending order using the reverse=True argument.
# sort() changes the original list directly.

students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr .Krabs"]

# students.sort()

sorted_students = sorted(students)

for i in sorted_students:
    print(i)

students_data = [("Henry", "F", 100), ("Clark", "C", 72), ("Hamilton", "A", 43)]

grade = lambda grade: grade[1]
sorted_data = sorted(students_data, key=grade)

for i in sorted_data:
    print(i)