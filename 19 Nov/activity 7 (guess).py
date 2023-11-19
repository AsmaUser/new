from random import randint
#guess= int (input ("guss the number: "))
guess= randint (1,30)
while (guess):
# while (guess<=20):
    if (guess==19):
        print("win",guess)
        break 
    else: 
        if (guess<19):   
            print("go up",guess)
            break
        else:
            if (guess>19):
                print("go down",guess)
                
            break 