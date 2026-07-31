prices_list=[]
def add_prices(prices_list,price):
    prices_list.append(price)
    print(f"{price} is added in prices list ")
def get_average_price(prices_list):
    total = 0
    average = 0
    if prices_list > 0:
        for x in prices_list:
            total += x
        average=total/len(prices_list)
        print(f"the average price is INR {average}")
    else:
        print("The list is empty")
def get_max_price(prices_list):
    x = 0 
    if prices_list > 0:
        for price in prices_list:
            if x < price :
                x = price
        print(f"maximum price is {x} in the list.")
    else:
        print("The list is empty")
x = ""
while x.lower() != "q" :
    print("""
    enter this choices
    1. Add price
    2. Show average price
    3. Show maximum price
    q. Quit""")
    x = input("Enter Choice : ")
    if x == "1":
        y = int(input("Enter a number to input: "))
        add_prices(prices_list,y)
    elif x == "2":
        get_average_price(prices_list)
    elif x == "3":
        get_max_price(prices_list)
    elif x.lower() == "q":
        print("Quitting...")
    else:
        print("Enter a valid number!") 