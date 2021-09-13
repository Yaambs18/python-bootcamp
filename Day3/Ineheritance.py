#Multilevel Inheritance

class Base():
	
	def __init__(self, name):
		self.name = name

	def getName(self):
		return self.name

class Child(Base):
	
	def __init__(self, name, age):
		Base.__init__(self, name)
		self.age = age

	def getAge(self):
		return self.age

class GrandChild(Child):
	
	def __init__(self, name, age, address):
		Child.__init__(self, name, age)
		self.address = address

	def getAddress(self):
		return self.address		

m = GrandChild("Yansh", 1, "Aligarh")
print(m.getName(), m.getAge(), m.getAddress())



#Mutiple inheritance

class Addition():
    def __init__(self):
        print("addition")  
    def Addition(self,a,b):  
        return a+b;  
    def func(self):
        print("this method is of addition class")

class Mulultiplication():  
    def __init__(self):
        print("multiplication")  
    def Multiplication(self,a,b):  
        return a*b
    def m1(self):
        print("this method is of multipication  class")
      
class Division(Addition, Mulultiplication):
    def __init__(self):
        print("divide")  
    def Divide(self,a,b):  
        return a/b;  



divide_ = Division()  
print(divide_.Addition(10,20))  
print(divide_.Multiplication(10,20))  
print(divide_.Divide(10,20))  
divide_.m1()