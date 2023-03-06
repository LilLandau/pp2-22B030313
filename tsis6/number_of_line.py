lines_number = 0

with open("test.txt") as f:
    lines_number = len(f.read().splitlines())

print("The number of lines is equal: ", lines_number)