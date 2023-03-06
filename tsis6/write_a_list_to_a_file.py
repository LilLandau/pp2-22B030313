l = ["Danial", "Akhmetgaliev"]

with open("list_into_file.txt", "w") as f:
    content = " ".join(l)
    f.write(content)