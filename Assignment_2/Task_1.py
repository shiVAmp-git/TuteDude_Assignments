# Task 1

order_amount = input("Enter bill amount:")
if type(order_amount) == str:
    print("Only Integers and Floats allowd")

if order_amount>=2000:
    discounted_price =order_amount- (order_amount*15)/100

elif 2000>order_amount>=1500:
    discounted_price = order_amount- order_amount/10

elif 1500>order_amount>=1000:
    discounted_price = order_amount - (order_amount*7)/100        

else:
    discounted_price = order_amount    

tax_price = discounted_price/20
billing_amount = discounted_price + tax_price

print(f"Discounted Price   : {discounted_price}")
print(f"Tax                : {tax_price}")
print(f"-------------------------------------")
print(f"Total Amount to Pay: {billing_amount}")