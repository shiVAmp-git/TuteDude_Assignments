class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price=price
        self.category=category
    def get_info(self):
        print(f"this is {self.name} it is in {self.category} category and its price is INR{self.price}")
    def apply_discount(self,discount):
        self.final_price =self.price - discount*self.price/100
        print(f"Final price for {self.name} is INR{self.final_price}")

bat = Product("Bat",2500,"Sports")
bat.get_info()
bat.apply_discount(10)
headphone = Product("headphone",2000,"Electronincs")
headphone.get_info()
headphone.apply_discount(20)
bat.name
