from easyinput import read
def collatz(n):
    if n==1: return 0
    else:
        if n%2==0: return 1 + collatz(n//2)
        if n%2!=0: return 1 + collatz(3*n+1)

n = read(int)

while n is not None:
    print(collatz(n))
    n = read(int)
