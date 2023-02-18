def generator_of_evens(n):
    for i in range(0, n, 2):
        yield str(i) + ","

n = int(input())
x = generator_of_evens(n)
