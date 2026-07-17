# Task 1
order_amount = 0 
order_amount_input = input("Enter bill amount:")
if order_amount_input.isdigit():
    order_amount = int(order_amount_input)
    print("You entered:",order_amount)
else:
    print("Please enter a valid number")    
    exit()

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