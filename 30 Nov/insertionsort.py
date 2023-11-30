def insertionsort(array):
    #tack key 
    for step in range (1, len(array)):
        key = array[step]
        j = step - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array [j]
            j = j-1
        
        array[j+1] =key
    
data = [6,2,1,3,4]
insertionsort(data)
print ("stored array in according order: ")
print (data)
