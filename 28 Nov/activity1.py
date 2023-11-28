try:
    x = int(input ("Enter a value of x: "))
    s = x/0
    print (s)
except ZeroDivisionError:
    print("Can't devide by zero")  