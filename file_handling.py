import os
import shutil

path = 'XYZ'


if os.path.exists(path):
    print("The path exists.")
    if os.path.isfile(path):
        print("It is a file.")
    elif os.path.isdir(path):
        print("It is a directory.")
else:
    print("The path does not exist.")


# Read a file

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

# Write a file

try:
    text = "Successfully written."
    with open('file.txt', 'w') as f:
        f.write(text)
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Append a file

text = '\nAppended.'

try:
    with open('file.txt', 'a') as f:
        f.write(text)
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Copy a file
dst_path = 'XYZ'

shutil.copyfile('file.txt', dst_path)

# Move a file

source = 'file.txt'
destination = 'XYZ'

try:
    if os.path.exists(destination):
        print("File already exists.")
    else:
        os.replace(source, destination)
except FileNotFoundError:
    print("The file was not found")

# Delete a file

path_info = '/Users/yashchaudhary/Desktop/done.txt'

try:
    if os.path.exists(path_info):
        # shutil.rmtree('xyz') : To remove non-empty folder
        # os.rmdir("xyz") : To remove empty folder
        os.remove(path_info)
    else:
        print('File was not found')

except FileNotFoundError:
    print("The File was not found")
except PermissionError:
    print('Permission denied.')
except OSError:
    print("You can not delete folder with files in that using rmdir cmd.")
else:
    print('Deleted successfully')





