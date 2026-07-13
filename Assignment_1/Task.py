# Task 1
products = ["Ball" , "Notebook" , "Cup" , "Ice-cream" , "Headphone" , "Purse"]
sample_product = ("Book" , 50 , "Stationery")

print(products[1::4])
products.append("Tablefan")
products.append("Shirt")

sample_product_list = list(sample_product)
sample_product_list[1] = 60
sample_product = tuple(sample_product_list)

# Task 2
categories_set = {"Sports" , "Stationery" , "kitchen-accessories" , "Dairy-product" , "Electronics" , "Fashion-accessories" , "Electrics" , "Fashion"}
categories_set.add("Mobile-accessories")
categories_set.add("Sports")
print(categories_set)
is_exist=False
if "Sports" in categories_set:
    is_exist = True
    print(is_exist)

else:
    is_exist = False
    print(is_exist)    

total_categories = categories_set.__len__()
print(f"there is total {total_categories} categories in set")    

# Task 3

price_dict = { "Ball": 10 , "Notebook" :60 , "Cup" : 150 , "Ice-cream" : 65 , "Headphone" : 2999 , "Purse" : 599 }
price_dict["Shirt"] = 799
price_dict["Cup"] = 250

for value in price_dict.values():
    value += value

avg_value = value/price_dict.__len__()    
print(f"Average Value is {avg_value:.2f}")

# Task 4

catalog = [("Ball" , 10 ,"Sports"),
           ("Notebook" , 60 , "Stationery"),
           ("Cup" , 250 , "Kitchen-accessories"),
           ("Ice-cream", 65 , "Dairy-product"),
           ("Headphone" , 2999 ,"Electronics"),
           ("Purse" , 599 , "Fashion-accessories"),
           ("Pencil" , 3 , "Stationery") ]

category_to_products= {}
for items in catalog:
   if items[2] not in category_to_products.keys():
       category_to_products[items[2]] = [items[0]]

   else:
       category_to_products[items[2]].append(items[0])


for key_x,value_x in category_to_products.items():
    for key_y,value_y in category_to_products.items():
        if category_to_products[key_x].__len__() >= category_to_products[key_y].__len__():
                    pass
        else :
             key_x = key_y
 
max_count = key_x
             

print(f"Your category who has most produt is {max_count}")


