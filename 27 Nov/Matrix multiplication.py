X = [[1,2,3],
     [6,7,8]]

Y = [[6,1],
     [2,10],
     [0,2]]
new_matrix = [[0,0,0],
              [0,0,0]]
for i in range (len (X)):
    
    for j in range (len(Y[0])):
        
        for k in range (len(Y)):
            new_matrix [i][j] += X[i][k]*Y[k][j]
for n in new_matrix:   
    print (n)
    
        

    
        
        
    
    