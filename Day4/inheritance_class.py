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