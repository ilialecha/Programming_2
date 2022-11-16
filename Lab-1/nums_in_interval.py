from easyinput import read
'''
procedure num_in_interval(a,b)
    if a <= b then
        for i=a up to b do
            if i != b then
                output i without new line
            else
                output i with new line
    else
        output an empty line
'''

def numininterval(a,b):
    if a <= b:
        for i in range(a,b+1):
            if i!= b : print(i,end=",")
            else: print(i)
    else: print()
        
a,b = read(int),read(int)

numininterval(a,b)