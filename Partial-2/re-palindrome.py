def palindrome(S):
    D = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    # Supposing that S tends to infinite, it's better to save length into a variable if we're using it at least twice.
    n = len(S)
    if n % 2 != 0: return False
    return rec_palindrome(S, 0, n-1, D)
def rec_palindrome(S, low, high, D):
    if low >= high: return True
    if S[low] == D[S[high]]: return rec_palindrome( S, low+1, high-1, D )
S = "AAATTT"
print(palindrome(S))



def comp(n, p, i):
    '''
    Computes K(n,p) = p + 2p + 3p + 4p + ... + np
    Worst case is when n at least is 2. If n <= 1 no need to do recursive calls so 0(1)
    Otherwise T(n) = T(n-1) + 0(1)
    '''
    if n == 0: return 0
    if n == 1: return p
    if i == n: return n*p
    return ( i*p ) + comp(n, p, i+1)

def comp2(n, p):
    '''
    Computes K(n,p) = p + 2p + 3p + 4p + ... + np
    Worst case is when n at least is 2. If n <= 1 no need to do recursive calls so 0(1)
    Otherwise T(n) = T(n-1) + 0(1)
    '''
    if n == 0: return 0
    if n == 1: return p
    return ( n*p ) + comp2(n-1, p)

def comp3(n,p):
    return p * comp3_r(n)
def comp3_r(n):
    #Base case
    if n == 1:
        return n
    return n + comp3_r(n-1)

print(comp3(997,1))