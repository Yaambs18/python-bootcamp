def cubes(n):
    for i in range(n):
        yield i**3

for i in cubes(10):
    print(i)

    