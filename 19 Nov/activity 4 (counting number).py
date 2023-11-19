#couting the numbers
v ="aoeui"
c = 0
m = input ("ENTER A TEXT: ")
for chr_1 in m:
    if (chr_1 in m):
        c+=1
print(c.isdigit(m))