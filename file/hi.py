"""file = open ("hi.txt","r")
count = 0
sum_=0
for line in file:
        sum_ += float(line)
        count += 1
print(sum_/count)"""
#To count the avarage 
# *********************************
"""input_file = open ("hi.txt", "r")
for line in input_file:
    line= line.rsplit(" ")
    print (line)"""
#To read from right to left
#-----------------------------------
#deling with list
"""input_file = open ("hi.txt", "r")
for line in input_file:
    line= line.rsplit(" ")
    print (line [0], "mark is :", line[1])"""
#**********************************************
"""input_file = open ("hi.txt", "r")
for line in input_file:
    line=(line.split(" "))
    if float(line[1]) > 70:
        print (line[0])"""
#***************************************