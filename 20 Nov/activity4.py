user_ans = (input("Enter YOUR answer= "))
ans = "abaacbb"
sum1= 0 
for i in range (len (ans)):
    if (ans[i]== user_ans[i]):
        sum1 +=1
print (sum1, "out of", len (ans))

         
    