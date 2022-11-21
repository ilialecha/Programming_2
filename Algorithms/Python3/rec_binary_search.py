def binary_search(A,x,l,h):
    while l < h:
        mid = (l+h)//2
        if A[mid] == x:
            return mid
        if A[mid] < x:
            l+=1
        if A[mid] > x:
            h-=1

def rec_binary_search(A,x,l,h):
    if l > h: return None
    mid = (l+h)//2
    if A[mid] == x: return mid
    if A[mid] < x:
        return rec_binary_search(A,x,l+1,h)
    else:
        return rec_binary_search(A,x,l,h-1)