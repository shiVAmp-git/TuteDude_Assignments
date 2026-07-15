# Task 1
products = ["Ball" , "Notebook" , "Cup" , "Ice-cream" , "Headphone" , "Purse", "pencil"]
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

price_dict = { "Ball": 10 , "Notebook" :60 , "Cup" : 150 , "Ice-cream" : 65 , "Headphone" : 2999 , "Purse" : 599 , "Pencil" : 5 , "Tablefan" : 1499 }
price_dict["Shirt"] = 799
price_dict["Cup"] = 250

for value in price_dict.values():
    value += value
   
avg_value = value/price_dict.__len__()    
print(f"Average Value is {avg_value:.2f}")

price = 0
for key,value in price_dict.items():
    if value > price:
        price = value
        product = key

print(f"{product} has maximum value which is {price}")

for keys,values in price_dict.items():
    if values < price:
        price = values
        min_product = keys

print(f"{min_product} has minimum value which is {price}")        
# Task 4
cat_map = { "Ball": "Sports" , "Notebook" : "Stationery" , "Cup" : "kitchen-accessories" , "Ice-cream" : "Dairy-product" , "Headphone" : "Electronics" , "Purse" : "Fashion-accessories" , "Pencil" : "Stationery" , "Tablefan" : "Electrics" , "Shirt" : "Fashion" }
catalog =[(p,price_dict[p],cat_map.get(p))  for p in price_dict]
category_to_products= {}
for items in catalog:
   if items[2] in category_to_products.keys():
       category_to_products[items[2]].append(items[0])

   else:
       category_to_products[items[2]] = [items[0]]

max_count = 1

for key_x,value_x in category_to_products.items():
    if value_x.__len__() > max_count:
        max_count = value_x.__len__()
        max_category = key_x    
      
             
print(f"{max_category}has most product is {max_count}")

