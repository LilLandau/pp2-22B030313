def generator_between_values(a, b):
    for i in range(a, b):
        yield pow(i, 2)


for i in generator_between_values(3, 10):
    print(i)