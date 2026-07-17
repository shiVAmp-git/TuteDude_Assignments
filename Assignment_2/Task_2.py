orders = [1200,2500,800,1750,3000]
revenue = 0
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
    revenue = revenue + amount
print(f"Total revenue is INR{revenue}")
i = 0 
for amount in orders:
     if amount>1000:
          i = i+1

print(f"there is total {i} orders who got discount")          