from collections import namedtuple

Dog = namedtuple('Dog', ['name', 'age', 'breed'])
sammy = Dog(name='sammy', age=3, breed='husky')

print(sammy.name)
print(sammy.age)
print(sammy.breed)
print(sammy)