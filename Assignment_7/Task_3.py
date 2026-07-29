class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price=price
        self.category=category
    def get_info(self):
        print(f"this is {self.name} it is in {self.category} category and its price is INR{self.price}")
class EletricProduct(Product):
    def __init__(self, name, price, category,warranty_years):
        super().__init__(name, price, category)
        self.warranty_years = warranty_years
    def get_info(self):
            print(f"this is {self.name} it is in {self.category} category and its price is INR {self.price} with warranty of {self.warranty_years} years")

iron = EletricProduct("Iron",1500,"Electronic",3)
iron.get_info()