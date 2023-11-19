nu=input ("Enter a number: ")
valid= len(nu) ==10
position= 0
#nu[0]=='+'
while valid and position <len(nu) :
    if nu== '+968':
        valid = ( (position == 0 and nu[position] == " ") or
                  (position == 4 and nu[position] == " ") or
                  (position == 8 and nu[position] == "-") or
                  (position != 0 and position != 4 and position != 8 and
                   nu[position].isdigit()))
        position = position +1
        print ("Not valid number")
else:
    print (" valid number")
        
        
        
   # for i in nu [8]:
      #print(input(),nu)
        
#else:
 #   nu != '+968'
  #  print ("valid number")
        
        
    