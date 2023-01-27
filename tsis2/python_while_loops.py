i = 1
while i < 6: #с левой границы [включительно] до правой (невключительно)
    print(i)
    i += 1
print("first result")

i = 1
while i < 6:
    print(i)
    if i == 3:
        break #выход с цикла при выполнении условия
    i += 1
print("second result")

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue #пропуск i при условии
    print(i)
print("third result")

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6") #выполняется при окончании цикла