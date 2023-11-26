m1 = [[0,5,1],
      [4,9,0],
      [0,6,0]]

m2=[[5,5,1],
    [5,8,1],
    [9,2,6]]

def func_1(mtx1,mtx2):
    new_matrix = []
    for row in range (len(mtx1)):
        rows=[]
        for coln in range (len(mtx1)):
            rows.append(mtx1[row][coln] + mtx2[row][coln])
        new_matrix.append(rows)
    print(new_matrix)
func_1(m1,m2)  

     
 