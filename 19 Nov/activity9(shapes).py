shape= int (input ("enter a number: "))

if (shape==1):
    sum_A=0
    def TrShip_A(sum_A):
        high= float (input("Enter H= "))
        base= float (input("Enter B= "))
        sum_A= (1/2)*high*base
        #print ('sum:',sum_A)
        return sum_A
    re=TrShip_A(sum_A)
    print(re)
    
elif(shape==2):
    sum_B=0
    def TrShip_B(sum_B):
        L= float (input("Enter L= "))
        sum_B= L**2
        #print ('sum:',sum_A)
        return sum_B
    res=TrShip_B(sum_B)
    print(res)
    
elif(shape==3):
    sum_C=0
    def TrShip_C(sum_C):
        r= float (input("Enter r= "))
        sum_C= 3.14*r**2 
        #print ('sum:',sum_A)
        return sum_C
    resl=TrShip_C(sum_C)
    print(resl)

elif(shape==4):
    sum_D=0
    def TrShip_D(sum_D):
        rr= float (input("Enter r= "))
        hh= float (input ("Enter h= "))
        sum_D= (2*3.14*rr*hh)+ (2*3.14*rr**2)
        #print ('sum:',sum_A)
        return sum_D
    reslt=TrShip_D(sum_D)
    print(reslt)
    
else:
    print ("stop here ")


        