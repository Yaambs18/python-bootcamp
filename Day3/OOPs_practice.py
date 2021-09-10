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



# magic/dunder methods

class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

b = Book('Python Rock', 'Jose', 200)
print(b)
print(len(b))        
# del b
# print(b)


# <------------------------------------------------------------------------>
# Exercises

#Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

class Line():

    def __init__(self, cord1, cord2):
        self.cord1 = cord1
        self.cord2 = cord2
    
    def distance(self):
        x1, y1 = self.cord1
        x2, y2 = self.cord2
        distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
        return distance
    def slope(self):
        x1, y1 = self.cord1
        x2, y2 = self.cord2
        return (y2-y1)/(x2-x1)

coordinate1 = (3,2)
coordinate2 = (8,10)
obj = Line(coordinate1,coordinate2)

print(obj.distance())
print(obj.slope())


# Fill in the class

class Cylinder:

    pi = 3.14    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return Cylinder.pi*self.radius**2*self.height
    
    def surface_area(self):
        return 2*Cylinder.pi*self.radius*(self.radius+self.height)

c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())


#Object Oriented Programming Challenge

class Account():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, deposit_amount):
        print("Deposit Accepted")
        self.balance += deposit_amount
    
    def withdraw(self, withdraw_amount):
        if withdraw_amount <= self.balance:
            print("Withdrawal Accepted")
            self.balance -= withdraw_amount
        else:
            print("Funds Unavailable!")

    def __str__(self):
        return f"Account owner : {self.owner} \nAccount balance : {self.balance}"

acct1 = Account('Jose',100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)      