class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price=price
        self.category=category
    def get_info(self):
        print(f"this is {self.name} it is in {self.category} category and its price is INR{self.price}")
    def __add__(self, other):
        print(f"Total price {self.name} and {other.name} is {self.price + other.price}")
class Inventory:
    def __init__(self):
        self.products =[]
    def add_product(self,product):
        self.products.append(product)
        print("Product added")       
    def remove_product(self,p_name):
        for product in self.products:
            if product.name == p_name:
                self.products.remove(product)
    def get_total_value(self):
        total = 0
        for product in self.products:
            total += product.price
        return f"Total price of all product is INR {total}"
    def show_all_products(self):
        for product in self.products:
            product.get_info()   

class Store:
    def __init__(self,store_name):
        self.store_name = store_name
        self.inventory = Inventory()
    def add_new_product(self):
        name = input("Enter name of the product: ")
        price = int(input("Enter price of the product: "))
        category = input("Enter category of the product: ")
        product = Product(name,price,category)
        self.inventory.add_product(product)
    def show_summary(self):
        print(f"Store Name: {self.store_name}")
        print(f"Total Product: {len(self.inventory.products)}")
        print(f"Total Value : {self.inventory.get_total_value()}")
store = Store("Patels Store")
store.add_new_product()
store.add_new_product()
store.add_new_product()
store.show_summary()
if len(store.inventory.products)>2:
    p1=store.inventory.products[0]
    p2=store.inventory.products[1]
    p1+p2