
num= int (input("Enter integer: "))
def  sumdigit(x):
    sum_1=0
    i=x
    while i != 0:
        sum_1 += i%10
        i = i//10
    
    return sum_1
result = sumdigit(num)
print (result) 

    