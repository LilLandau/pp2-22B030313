import re

string = input("Enter the string in snake_case: ")
string = re.sub('([A-Z]+)', r'_\1', string).lower()

print(string[1:])