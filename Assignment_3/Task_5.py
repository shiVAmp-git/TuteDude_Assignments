price = [100,250,400,1200,50,2000,850]
def grt_500(x) :
    if x > 500:
        return True
    else :
        return False
def les_500(x):
    if x < 500:
        return True
    else :
        False
Grater = filter(grt_500,price)
Less = filter(les_500,price)

print(list(Grater))
print(list(Less))

    