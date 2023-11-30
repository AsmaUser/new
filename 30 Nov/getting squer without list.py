def binary_search (x):
    li, hi =1, x
    if (x == 1 or x ==0):
        return x
    while(li<=hi):
        # using // to avoid points
        mid = (hi+li)//2
        if(mid*mid == x):
            return mid
        elif(mid*mid < x):
            li = mid +1
        else:
            hi = mid -1
    return -1

num = int(input("Enter a number: "))
target = binary_search(num)
print (target)
