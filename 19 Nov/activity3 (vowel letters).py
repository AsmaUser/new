#vowel letters
v ="a,o,e,i"
c = 0
m = input ("ENTER A TEXT: ")
for chr_1 in m:
    if (chr_1 in v):
        c+=1
print(c)