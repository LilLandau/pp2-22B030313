import shutil

file1 = input("Write name of the origin file: ")
file2 = input("Give name to the copy file: ")

shutil.copy(file1 + ".txt", file2 + ".txt")