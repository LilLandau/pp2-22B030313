import re

file = open("row.txt", encoding="utf-8")
text = file.read()
text = text.split()

inclusions = []
pattern = r"ab*"                            #ноль или более вхождения символа b
for word in text:
    if re.fullmatch(pattern, word):         #проверка по ПОЛНОМУ совпадению по патерну
        inclusions.append(word)

if len(inclusions) == 0:
    print("no matches in text")
else:
    print("the matches: ", ",".join(inclusions))

    