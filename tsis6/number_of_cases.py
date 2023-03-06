import string

s = input("Input the string: ")

up = 0
low = 0
for c in s:
    if c.isupper():
        up = up + 1
    elif c.islower():
        low = low + 1

print("The number of uppercase letters:", up, "\nAnd lowercase letters:", low)