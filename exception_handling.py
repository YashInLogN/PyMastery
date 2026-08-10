# exception = Exception handling is a crucial aspect of programming that allows developers to manage and respond to errors or unexpected situations that may arise during the execution of a program. In Python, exceptions are raised when an error occurs, and they can be caught and handled using try-except blocks.

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
except ValueError:
    print("Please enter valid integers.")
except ZeroDivisionError:
    print("Denominator cannot be zero.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print(f"The result is: {result}")
finally:
    print("Execution completed.")


# all exceptions that can be raised in python are listed below:
# ValueError: Raised when a function receives an argument of correct type but inappropriate value.
# ZeroDivisionError: Raised when the second operand of a division or modulo operation is zero.
# TypeError: Raised when an operation or function is applied to an object of inappropriate type.
# NameError: Raised when a local or global name is not found.
# IndexError: Raised when the index of a sequence is out of range.
# KeyError: Raised when a dictionary key is not found.
# FileNotFoundError: Raised when a file or directory is not found.
# PermissionError: Raised when the user does not have permission to perform the requested operation.
