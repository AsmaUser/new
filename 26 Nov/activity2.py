from typing import List
def revarse_list(my_list:List[int])->int: 
    return my_list.pop()
new_list= int ([1,5,6])
ls = revarse_list(new_list)
#print (revarse_list(new_list))
print (ls)