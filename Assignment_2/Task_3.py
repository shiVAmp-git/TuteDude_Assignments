n = ""
orders = []
while n.lower()!="q":
    print("""Menu Options:
    1 - Add order amount to a running list
    2 - Show all orders and totals after applying discounts
    q - Quit""")
    n = input("Enter your choice: ")

    if n== "1" : 
        number = int(input("Enter Amount"))
        orders.append(number)

    elif n== "2" :
        print("| Order Amount | discount% | Final Amount ")
        for amount in orders:
            if amount>=2000:
                discount = 15
                final_amount =amount- (amount*discount)/100

            elif 2000>amount>=1500:
                discount = 10
                final_amount = amount- amount/discount

            elif 1500>amount>=1000:
                discount = 7
                final_amount = amount - (amount*discount)/100        

            else:
                discount = "0%"
                final_amount = amount    
            print(f"| {amount} | {discount}% | {final_amount} |")

    elif n=="q" :
        print("Quitting...")

    else:
        print("Inalid Input")     