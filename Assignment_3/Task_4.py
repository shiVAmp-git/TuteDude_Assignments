price = [100,250,400,1200,50]
gst = lambda price : price+ 0.18* price

x= map(gst,price)
print(price)
print(list(x))