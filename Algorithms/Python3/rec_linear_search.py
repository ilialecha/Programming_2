def linear_search(A, x, low, high):
    i = low
    while i <= high and A[i]!=x:
        i += 1
    if i > high: return None
    return i

def rec_linear_search(A,x,l,h):
    if l > h: return None
    if A[l] == x: return l
    else: return rec_linear_search(A,x,l+1,h)
    