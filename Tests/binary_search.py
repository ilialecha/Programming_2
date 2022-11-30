'''
[1,2,3,4,5,6,7,8,9,10]
 L                  H
 -->              <--
 L=0 and  H=|S| ==> mid =
'''

def binary_search(A, x, low, high):
    if low >= high: return -1
    mid = (low+high)/2
    if x == A[mid]: return mid 
    if x > A[mid]: return binary_search(A,x,low,mid-1)
    else: return binary_search(A,x,mid+1,high)

'''
 1,2,3,4,5
 0,1,2,3,4
'''
def print_array(A,index,limit):
    if limit - index > 0:
        print(A[index])
        return print_array(A,index+1,limit)  
A = [1,2,3,4,5,6]
print_array(A,0,len(A))

def count_digits(n):
    if n <= 9: return 1
    return 1 + count_digits(n//10)

print(count_digits(1000))