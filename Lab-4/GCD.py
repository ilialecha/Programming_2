'''
function GCD(A, B)
    if A = 0 then
        return B
    if B = 0 then 
        return A
    if a > b then
        return GCD(B, A MOD B)
    else
        return GDC(A, B MOD A)
''' 
from easyinput import read
def GCD(A,B):
    
    if A == 0: return B
    if B == 0: return A
    if A > B :
        return GCD(B, A % B)
    else:
        return GCD(A, B % A)

A,B = read(int),read(int)
while A is not None and B is not None:
    print(GCD(A,B))
    A,B = read(int),read(int)
