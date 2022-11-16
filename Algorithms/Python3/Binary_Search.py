'''
    FUNCTION binary-search(A,low,high,x):
        while low <= high do
            mid = (low + high) /2
            if x = A[mid] then
                return mid
            else if x > A[mid] then
                low = low + 1
            else
                high = high - 1
        return nil
'''
def binary_search(a, low, high, x):
    while low <= high:
        mid = (low + high) // 2
        if x == a[mid]: return mid
        elif x > a[mid]: low += 1
        else: high -= 1
    return -1

a = [1, 2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10]
low = 2
high = 8 

bs = binary_search(a, low, high, 4)

if bs != -1: print(4," is at position ",bs)

