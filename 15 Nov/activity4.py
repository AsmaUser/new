time=float(input("Enter time : "))
partOfDay = input("Is it AM or PM?")
if (partOfDay.lower() == "am"):
 if (time<8):
  print("before 8:00 Am")
 else: 
    print("8:00 AM")
elif (partOfDay.lower() == "pm"):
     if (time<8):
      print ("before 8:00 Am")
     else: 
         print("Invlid")
    
