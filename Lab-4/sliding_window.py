from easyinput import read_line,read

'''
Pseudocode

PROCEDURE sliding_window(sequence, x, y):
    n = len(sequence)
    for i=1 to n by step y do
        if i+x <= n do 
            SHOW sequence[i : i+x]
'''

def sliding_window(sequence,x,y):
    for i in range(0, len(sequence),y):
        if i+x <= len(sequence): print(sequence[i:i+x])

s = read_line()
x,y = read(int),read(int)

sliding_window(s, x, y)

#ACGGTAGACCT
'''
ACG
CGG
GGT
GTA
TAG
AGA
GAC
ACC
CCT
'''