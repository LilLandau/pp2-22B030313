import re

string = input("Enter the string")
pattern = r"[ .,]"

print(re.sub(pattern, ":", string))
