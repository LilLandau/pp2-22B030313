thisset = {"apple", "banana", "cherry"}
print(thisset)      #вывод множества

#множество содержит в себе только уникальные значения
thisset = {"apple", "banana", "cherry", "apple"} 
print(thisset) 

print(len(thisset)) #вывод длины

set1 = {"abc", 34, True, 40, "male"} #множество может содержать разные типы данных

myset = {"apple", "banana", "cherry"}
print(type(myset))          #вывод типа

thisset = set(("apple", "banana", "cherry")) #конструктор множества
print(thisset) #обязательные двойные скобки

#элементы множества являются НЕИЗМЕНЯЕМЫМИ