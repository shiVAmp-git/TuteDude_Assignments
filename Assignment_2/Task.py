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
print("""           /
          Task 2
             /""")
orders = [1200,2500,800,1750,3000]
print("| Order Amount | discount% | Final Amount ")
for amount in orders:
    if amount>=2000:
         discount = "15%"
         final_amount =amount- (amount*15)/100

    elif 2000>amount>=1500:
         discount = "10%"
         final_amount = amount- amount/10

    elif 1500>amount>=1000:
         discount = "7%"
         final_amount = amount - (amount*7)/100        

    else:
         discount = "0%"
         final_amount = amount    

    print(f"| {amount} | {discount} | {final_amount} |")

# Task 3
n = ""
while n.lower()!="q":
  print("""Menu Options:
    1 - Add order amount to a running list
    2 - Show all orders and totals after applying discounts
    q - Quit""")
  n = input("Enter your choice: ")

  match(n.lower()):
      case "1" : 
          number = int(input("Enter Amount"))
          orders.append(number)

      case "2" :
          print("| Order Amount | discount% | Final Amount ")
          for amount in orders:
              if amount>=2000:
                 discount = "15%"
                 final_amount =amount- (amount*15)/100

              elif 2000>amount>=1500:
                   discount = "10%"
                   final_amount = amount- amount/10

              elif 1500>amount>=1000:
                   discount = "7%"
                   final_amount = amount - (amount*7)/100        

              else:
                   discount = "0%"
                   final_amount = amount    

              print(f"| {amount} | {discount} | {final_amount} |")

      case "q" :
          print("Quitting...") 