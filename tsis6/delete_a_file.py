import os

file_name = input("Name of the file: ")
location = input("Path to the file: ")

if os.access(location, os.F_OK) is True and os.access(os.path.join(location, file_name), os.F_OK):
    os.remove(os.path.join(location, file_name))
else:
    print("Such path or file doesn't exists")