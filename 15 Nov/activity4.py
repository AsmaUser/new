time=float(input("Enter time : "))
minutes= int(input("Enter minutes: "))
partOfDay = input("Is it AM or PM?")
if (partOfDay.lower() == "am"):
 if time<8 or (time ==8 and minutes == 0):
  print("before 8:00 Am")
 else: 
    print("8:00 AM")
elif (partOfDay.lower() == "pm"):
     if time<8 or (time ==8 and minutes == 0):
      print ("After 8:00 Am")
     else: 
         print("Invlid")
    
