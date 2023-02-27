import re
file = open("row.txt", encoding="utf-8")
text = file.read()
text = text.split()

inclusions = []
pattern = r"[A-Z][a-z]+$"

for word in text:
    if re.search(pattern, word):         
        inclusions.append(word)

if len(inclusions) == 0:
    print("no matches in text")
else:
    print("the matches: ", ", ".join(inclusions))

