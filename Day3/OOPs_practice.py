class Dog():
    species = "mammal"
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name

        self.spots = spots
    
    def bark(self):
        print("Woof! My name is {}".format(self.name))

my_dog = Dog('Lab', 'Sammy', 'Nospots ')
print(type(my_dog))
print(my_dog.breed)
print(my_dog.species)
print(my_dog.name)
print(my_dog.spots)
my_dog.bark()