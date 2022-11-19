from easyinput import read

def fibonacci(n,m):
    if n<= 1: return n
    else: return fibonacci(n-1,m) + fibonacci(n-2,m)

n,m = read(int),read(int)

while n is not None and m is not None:
    print(fibonacci(n,m))
    n,m = read(int),read(int)

