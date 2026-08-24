# Lambda functions are small, anonymous functions defined using the lambda keyword.
# They can take any number of arguments but contain only a single expression.
# Lambda functions are useful for short, simple operations.

# def double(x):
#     return x*2

# result = double(2)
double = lambda x: x * 2

print(double(4))