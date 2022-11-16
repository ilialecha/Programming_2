def rec_factorial2(n):
    if n == 0: return 1
    else: return n*rec_factorial2(n-1)

def it_factorial(n):
    r = 1
    for i in range(n,1,-1): r*=i
    return r
