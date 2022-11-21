def digits(n):
    i=0
    while n > 9:
        i+=1
        n = n//10
    return i+1
def r_digits(n):
    if n <= 9: return 1
    else: return 1+digits(n//10)