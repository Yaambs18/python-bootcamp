class Dog():
    species = "mammal"
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name

        self.spots = spots
    
    def bark(self):
        return ("Woof! My name is {}".format(self.name))
