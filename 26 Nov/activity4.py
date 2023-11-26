def func_read(n):
    result= []
    for i in range (n):
        num = float(input("Enter a number: "))
        result.append (num)
    return result

def multipli_fun(ls, factor):
    for i in range (len(ls)):
        ls[i]= ls[i]*factor
    return ls 
           
def print_reverse(ls):
    ls.reverse()
    return ls 

def main ():
    my_list= func_read(4)
    factor_num= int (input ("Enter the factor: "))
    new_list=multipli_fun(my_list, factor_num)
    final_list= print_reverse(new_list)
    print (final_list)
    
main ()   
    
