import os
os.system('cls')

class Product:
    def __init__(self,name,price) -> None:
        self.name=name
        self.price=price
    
    def __add__(self,other):
        print("Add operator called")
        print(f"Added result: {self.price+other.price}")

    def __sub__(self,other):
        print("Subtract operator called")
        print(f"Subtarcted result: {self.price-other.price}")
    
obj1=Product("Iphone 7",38000)
obj2=Product("Redmi 11T",20000)

obj1+obj2
print()
obj1-obj2