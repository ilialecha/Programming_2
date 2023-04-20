from easyinput import read

def rec_collatz(n):
    if n == 1 : return 0
    return 1 + rec_collatz(n/2) if n % 2 == 0 else 1 + rec_collatz((n*3)+1)
'''
n = read(int)
while n is not None:
    print(rec_collatz(n))
    n = read(int)
'''

import sys 

def rec_polynomial(x, coef, coefMax, index):
    if index == coefMax:
        return float( coef[ index ] ) * ( x**index )
    return float( coef[index] ) * (x**index) + rec_polynomial(x,coef, coefMax, index+1)
    
x = float(sys.stdin.readline())
coef = sys.stdin.readline().split()
print("{:.4f}".format(rec_polynomial( x, coef, len( coef )-1, 0 ) ) )
