file1 = input("Write name of the origin file: ")
file2 = input("Give name to the copy file: ")

with open(file1 + ".txt") as f, open(file2 + ".txt", "w") as w:
    for line in f:
        w.write(line)