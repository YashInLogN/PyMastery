# Lambda functions are small, anonymous functions defined using the lambda keyword.
# They can take any number of arguments but contain only a single expression.
# Lambda functions are useful for short, simple operations.

# def double(x):
#     return x*2

# result = double(2)
double = lambda x: x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y+ z
full_name = lambda first_name, last_name: first_name + " " + last_name
age_check = lambda x: True if x >= 18 else False

print("Double: ", double(4))
print("Multiply: ", multiply(3, 4))
print("Addition: ", add(3, 4, 5))
print("Full_name: ", full_name(first_name:= input("First_name: "), last_name:= input("last_name: ")))
print("Age_check: ", age_check(age := int(input("Enter your age: "))))