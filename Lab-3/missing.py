from sys import stdin

import easyinput


'''
function is_missing():

'''

def is_missing(line):
    line = line.split()
    i=1
    for i in range(1,int(line[0])+1):
        if str(i) not in line[1:]: return print(i)

line = easyinput.read_line()

while line is not None:
    is_missing(line)
    line = easyinput.read_line()


'''
C = {
    A:T
    C:G
}
C[0] 
C[A]

A A T T T
0 1 2  3 4



C[S[low]]
'''