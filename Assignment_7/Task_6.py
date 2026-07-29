class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price=price
        self.category=category
    def get_info(self):
        print(f"this is {self.name} it is in {self.category} category and its price is INR{self.price}")
    def __str__(self):
        return f"this product is {self.name} it covered in {self.category} category with price INR {self.price}"
    def __add__(self, other):
        return f"this both proucts' total price is {self.price} "
bat = Product("Bat",2500,"Sports")
headphone = Product("headphone",2000,"Electronincs")
print(bat.__add__(headphone))