import os

path = '/Users/yashchaudhary/Desktop/test/text.txt'

# path = '\\Users\\yashchaudhary\\Desktop\\test' 

# if os.path.exists(path):
#     print("The path exists.")
#     if os.path.isfile(path):
#         print("It is a file.")
#     elif os.path.isdir(path):
#         print("It is a directory.")
# else:
#     print("The path does not exist.")

try:
    f = open(path, 'r')
    content = f.read()
    f.close()
except FileNotFoundError:   
    print("The file was not found.")
else:
    print("File content:")
    print(content)
finally:
    print(f"File closed: {f.closed}")  # This will print True if the file was closed successfully, False otherwise.
    print("File handling operation completed.")