def generator_division(N):
    for i in range(0, N):
        if i % 3 == 0 and i % 4 == 0:
            yield i 

N = int(input())
x = generator_division(N)

for i in x:
    print(i)