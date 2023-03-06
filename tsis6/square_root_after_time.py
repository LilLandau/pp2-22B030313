from time import sleep
import math

num = int(input("Enter the number: "))
time = int(input("Enter the time in milliseconds: "))

sleep(time / 1000)
s = "Square root of {0} after {1} miliseconds is {2}".format(num, time, math.sqrt(num))
print(s)
