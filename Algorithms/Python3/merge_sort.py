def merge(A,p,q,r):
    nl = q - p +1
    nr = r - q
    l1 = A[0:nl-1]
    l2 = A[0:nr-1]
    for i in range(nl):
        l1 = A[p+1]
    for i in range(nr):
        l2 = A[q+i+1]
    i, j = 0, 0
    k = p
    while i < nl and j < nr:
        if l1[i] <= l2[i]:
            A[k] = l1[i]
            i+=1
        else:
            A[k] = l2[j]
            j+=1
        k+=1
    while i < nl:
        A[k] = l1[i]
        i+=1 ; k+=1
    while j < nr:
        A[k] = l2[j]
        j+=1 ; k+=1



def mergeSort(A,p,r):
    # Size of A would be 1.
    if p>=r: return A[p:r+1]
    # Half of the length.
    q = (p+r)//2
    # Mergesort the lower part
    mergeSort(A,p,q)
    # Mergesort the upper part
    mergeSort(A,q+1,r)
    # Combine lower and upper.
    merge(A,p,q,r)

def merge_Sort(A):
    mergeSort(A,0,len(A))

l = [9,8,7,6,5,4,3,2]

merge_Sort(l)