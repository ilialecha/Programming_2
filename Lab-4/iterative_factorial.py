'''
Pseudocode:

FUNCTION factorial(n):
    Let R equal 1
    for i=n down to 1 do
        R = R*i
    return R
'''

def factorial(n):
    r = 1
    for i in range(n,1,-1): r*=i
    return r
