class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.__price=price
        self.category=category
    def get_price(self):
        print(f"Price of {self.name} is INR{self.__price}")    
    def set_price(self,price):
        if price>0 :
            self.__price = price
        print(f"Updated price for {self.name} is INR{self.__price}")    

p1 = Product("Bat",3400,"Sports")
p1.get_price()
p1.set_price(4500)