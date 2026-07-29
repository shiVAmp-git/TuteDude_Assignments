class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price=price
        self.category=category
    def get_info(self):
        print(f"this is {self.name} it is in {self.category} category and its price is INR{self.price}")
class Mobile(Product):
    def __init__(self, name, price, category):
        super().__init__(name, price, category)
    def get_info(self):
        print(f"this mobiles name is {self.name} and this is comes under {self.category} category with price of INR {self.price}")
class Laptop(Product):
    def __init__(self, name, price, category):
        super().__init__(name, price, category)
    def get_info(self):
        print(f"this laptop is good performance laptop which is {self.name} it is comes under {self.category} category with price of INR {self.price}")
m1 = Mobile("Samsung S26 Ultra", 150000 , "Smartphone")
l1 = Laptop("Dell Latitude 5480", 80000 , "Laptop")
object_list=[m1,l1]
for x in object_list:
    x.get_info()
       