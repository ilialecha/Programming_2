from easyinput import read_line,read
def reverse_input(n, prev):
    new_input = read_line()                   
    if n == 0:
        return ( prev ) 
    
    else:
        if n == -1 :
            reverse_input( new_input , "")
            return( prev )
        else:
            print (reverse_input( n - 1, new_input ))
            return( prev )

reverse_input("",read(int))