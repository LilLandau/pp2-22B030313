x = input("Enter the boolean values of tuple: ").split()
x = tuple(map(eval, x))

print(all(x))