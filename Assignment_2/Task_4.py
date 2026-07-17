daily = [200,150,0,400,50,-1,300]
total_sales = 0
for item in daily:
    if item <0 :
        break
    elif item == 0:
        continue
    else :
        total_sales = total_sales + item
print(f"Total sales are {total_sales}")
