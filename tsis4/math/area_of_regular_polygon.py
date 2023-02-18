from math import *

number_of_sides = int(input("Input number of sides:"))
side_lenght = int(input("Input the length of a side:"))

area = (number_of_sides * pow(side_lenght, 2)) / (4 * tan(pi / number_of_sides))

print(int(area))