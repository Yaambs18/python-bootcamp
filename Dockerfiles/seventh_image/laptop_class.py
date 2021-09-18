class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def apply_discount(self, n):
        return (self.price - n*self.price/100)

# ob1 = Laptop('dell', 'e7240', 45000)
# ob2 = Laptop('hp', 'axus', 55000)
# print(ob2.apply_discount(50))
