fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)        #пробежка по элементам списка

for x in "banana":
    print(x)        #пробежка по буквам в строке


for x in fruits:
    print(x)
    if x == "banana":   #условие выхода из цикла, если элемент равен строке banana
        break           #cherry не будет выводиться, в силу позиционирования break

for x in fruits:
    if x == "banana":
        break           #banana и cherry не будут выводиться, в силу поз. break
    print(x)        

for x in fruits:
    if x == "banana":
        continue    #не выводить banana
    print(x)


for x in range(6):
    print(x)        #вывод чисел от 0 до 5

for x in range(2, 30, 3):
    print(x)        #вывод чисел от 2 до 29 с шагом в 3 единицы


for x in range(6):
    print(x)
else:
    print("Finally finished!") #выведится при окончании цикла


for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")    #не выведится, т.к. произошел выход из цикла


adj = ["red", "big", "tasty"]

for x in adj:
    for y in fruits:
        print(x, y)             #вложенные циклы


for x in [0, 1, 2]:
    pass                        #использование pass'а


