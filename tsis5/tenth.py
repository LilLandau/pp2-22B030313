import re

string = input("Enter the word in snake_case: ")
string = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", string)
string = re.sub('([a-z0-9])([A-Z])', r'\1_\2', string).lower()
print(string)