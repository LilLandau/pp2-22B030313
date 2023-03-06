import os

p = input("Write a path: ")

for current_dir, dirs, files in os.walk(p):
    print(current_dir, dirs, files)
