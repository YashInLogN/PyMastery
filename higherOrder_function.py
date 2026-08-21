# Higher Order Function = a function that either: 
#                             1. accepts a function as an argument
#                             or returns a function
#                      (In python, functions are also treated as objects)

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def change(func):
    data = func(text := input("Enter the text: "))
    print(data)

change(quiet)