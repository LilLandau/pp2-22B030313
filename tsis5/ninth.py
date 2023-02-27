import re

string = input("Enter the word in CamelCase: ")
pattern = r"(\w)([A-Z])"
print(re.sub(pattern, r"\1 \2", string))        #где в replace 1 и 2 - группы в pattern