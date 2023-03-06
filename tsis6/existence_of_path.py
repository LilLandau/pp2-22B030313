import os

p = input("Write a path: ")
print("Existence of the path: ", os.path.exists(p))

if os.path.exists(p) is True:
    print("Inside of directory: ", os.listdir(p))
    print("The path to directory: ", os.path.dirname(p))
    print("The name of the directory: ", os.path.basename(p))