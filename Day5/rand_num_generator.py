import random
def rand_num(low,high, n):
    for i in range (n):
        yield random.randint(low,high)

for num in rand_num(1,50,5):
    print(num)