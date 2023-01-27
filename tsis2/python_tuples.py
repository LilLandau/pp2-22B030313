thistuple = ("apple", "banana", "cherry")   #создаем кортеж
print(thistuple)            #вывод кортежа

thistuple = ("apple", "banana", "cherry", "apple", "cherry")    
print(thistuple)       #в кортеже могут повторяться элементы

print(len(thistuple))

thistuple = ("apple",)  #для создания кортеже с 1 эл. нужна обязательная запятая
print(type(thistuple))

tuple1 = ("abc", 34, True, 40, "male")  #в кортеже могут быть разные типы данных

thistuple = tuple(("apple", "banana", "cherry")) # конструктов кортежа
print(thistuple)    #обязательные двойные скобки

#кортеж является НЕИЗМЕНЯЕМЫМ типом данных