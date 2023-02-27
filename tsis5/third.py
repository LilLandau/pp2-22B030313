import re

string = "Enter the word in snake_case: "
pattern = r"[a-z]+_[a-z]+"
print(re.findall(pattern, string))

