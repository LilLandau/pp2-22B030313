thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict) #вывод словаря

print(thisdict["brand"]) #доступ к значению через ключ

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020      #данные просто перезапишутся на более поздние
}
print(thisdict)     

print(len(thisdict)) #доступ к длине

#словарь может содержать разные типы данных
thisdict =	{
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
} 

print(type(thisdict))   #вывод типа

#конструкток словаря
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)