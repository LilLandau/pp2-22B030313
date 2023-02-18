def generator_desc(n):
    for i in range(n, 0, -1):
        yield i

for i in generator_desc(10):
    print(i)