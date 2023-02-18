def generator_of_squares(N):
    for i in range(N):
        yield pow(i, 2)

N = int(input())
x = generator_of_squares(N)

for i in x:
    print(i)