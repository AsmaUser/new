# i=0
n =int(input("->"))
sum_ = 0
while (n !=0):
#     sum_+=it (n[i])
    sum_+= n%10
    n= n//10
#     i+=1
print(sum_)
    