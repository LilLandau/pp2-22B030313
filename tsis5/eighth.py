import re

string = input("Enter the string in CamelCase: ")
pattern = r"[A-Z][^A-Z]*"

words = re.findall(pattern, string)
print(words)

