import random

x = 1
y = 2.8
z = 1j

print(type(x), type(y), type(z))

x = 1
y = 35656222554887711
z = -3255522
print(type(x), type(y), type(z))

x = 1.10
y = 1.0
z = -35.59
print(type(x), type(y), type(z))

x = 35e3
y = 12E4
z = -87.7e100
print(x, y, z)
print(type(x), type(y), type(z))

x = 3+5j
y = 5j
z = -5j
print(type(x), type(y), type(z))

x = 1
y = 2.8
z = 1j

a = float(x)
b = int(y)
c = complex(x)
print(a, b, c)
print(type(a), type(b), type(c))

print(random.randrange(1, 10))