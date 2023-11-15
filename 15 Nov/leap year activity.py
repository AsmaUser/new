# to get the year from the user 
year= int (input ("Enter year: "))
#divided by 100 means century year (ending with 00)
#The century year divided by 400 is leap year
if (year % 400 ==0) or (year % 100 != 0 and year % 4 == 0):
    print("{0} is a leap year".format(year))
    
#not divided by 100 means not centry year
# year divided by 400 is leap year

# elif (year % 400 ==0) and (year % 100 ==0):
#     print ("{0} is a leap year".format(year))
#if not divided by both 400 and 4 not century year
#year is not leap year
else:
    print("{0} is not a leap year".format(year))
    

  