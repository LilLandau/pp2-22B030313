import re

file = open("row.txt", encoding="utf-8")
text = file.read()
text = text.split()

inclusions = []
pattern = r"ab{2-3}"                        #от 2 до 3 (включительно) b
for word in text:
    if re.fullmatch(pattern, word):         #проверка по ПОЛНОМУ совпадению по патерну
        inclusions.append(word)

if len(inclusions) == 0:
    print("no matches in text")
else:
    print("the matches: ", ",".join(inclusions))