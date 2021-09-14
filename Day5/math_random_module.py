import math

math.floor(4.7)
print(math.ceil(4.2))

print(round(5.5))

print(math.log(math.e))

print(math.log10(10000000))



# ---------------------------------------------------------

import random

print(random.randint(1,100))
print(random.randint(1,100))
# print(random.randint(1,100))
# print(random.randint(1,100))

# for i in range(2):
#     random.seed(101)
#     print(random.randint(1,100))
#     print(random.randint(1,100))
#     print(random.randint(1,100))
#     print(random.randint(1,100))

l = [1,2,3,4,5,6,7]
print(random.choice(l))

print(random.choices(population=l, k=5))  # with repitition

print(random.sample(population=l, k=6)) # without repitition


#random decimal number 
print(random.uniform(0,100))