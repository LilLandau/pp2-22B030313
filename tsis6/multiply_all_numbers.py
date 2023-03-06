from functools import reduce

x = input("Write the numbers: ").split()
x = list(map(int, x))

result_of_multiply = reduce(lambda num1, num2: num1*num2, x)

print("The result of multiplying all numbers: ", result_of_multiply)