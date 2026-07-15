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