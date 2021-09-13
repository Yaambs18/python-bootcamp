class UnAcceptedValueError(Exception):   
    def __init__(self, data):    
        self.data = data
    def __str__(self):
        return repr(self.data)


try:
    Num_of_Sections = int(input("Enter Num of Sections: "))
    if(Num_of_Sections < 1):
        raise UnAcceptedValueError("Number of Sections can't be less than 1")
except UnAcceptedValueError as e:
    print ("Error:", e.data)