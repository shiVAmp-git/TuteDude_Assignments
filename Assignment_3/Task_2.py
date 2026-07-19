def factorial(n):
    if n == 0 or n==1:
        return 1
    elif n<0 :
        return print("Invalid Number")
    else:
        num = int(n)
        return num * factorial(num-1)
    

factorial(-3)