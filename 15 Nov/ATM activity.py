PIN=int (input ("Enter your PIN: "))
Balance=1000
# process= 1, 2,3
# print(process)
if PIN==1234 :
    process=int (input(" 1-Chack Balance, 2-Withdraw money, 3-Deposit money: "))
    if process==1:
     print (Balance)
    else:
#         print (process)
        if process==2:
             widMon=int (input ("Enter money amount: "))
             print(Balance-widMon)
        else:
#              print (process)
             if process==3:
                depMon= int (input ("Enter money amount: "))
                print(Balance+depMon)
             else:
                 print("Try gain")
             
else:
     print("Wroung Number")
    
