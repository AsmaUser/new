pin= 0
Balance=1000
while (pin==pin):
    pin= int (input("Enter Pass: "))
    if (pin ==1234):
        proc= int (input("1-Chack Balance, 2-Withdraw money, 3-Deposit money, 4-FINISH:"))
        if proc==1:
            print (Balance)
#         continue
        elif proc==2:
            widMon=int (input ("Enter money amount: "))
            print (Balance-widMon)
#         continue    
            
        elif proc==3:
            depMon= int (input ("Enter money amount: "))
            print(Balance+depMon)
#         continue
        elif proc==4:
            print ("Finish")
        break
    else:
        print("Try again")
     
        
            