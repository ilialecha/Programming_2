'''
'''
def bubblesort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]

def bubblesort2(a):
    n = len(a)
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if a[j] < a[j-1]:
                a[j],a[j-1] = a[j-1],a[j]

def binary_search(a,lo,hi,x): #HAS TO BE ORDERED ARRAY!!!
    while lo <= hi:
        mid = (lo+hi)//2
        if x == a[mid]: return mid
        elif x > a[mid]: lo+=1
        else: hi-=1
    return -1

def insertionsort(a):
    n = len(a)
    for i in range(1,n):
        k = a[i]
        j = i-1
        while j>=0 and a[j]>k:
            a[j+1] = a[j]
            j-=1
        a[j+1] = k

def insertion_sort(a):
    for i in range(1,len(a)):
        k = a[i]
        j = i-1
        while j>=0 and a[j] > k:
            a[j+1] = a[j]
            j-=1
        a[j+1] = k

def selection_sort(a):
    n = len(a)
    for i in range(n-1):
        s = i
        for j in range(i+1,n):
            if a[j] < a[s]: s = j 
        a[i],a[s] = a[s],a[i]


def linear_search(a,x):
    i=0
    while i <= len(a) and x != a[i]: i+=1
    if i>len(a): return print("No found")
    return print("Found at ",i)


a = [9,8,7,6,5,4,3,2,1,0]
bubblesort(a)
print(a)
a = [9,8,7,6,5,4,3,2,1,0]
bubblesort2(a)
print(a)



'''
PROCEDURE selection-sort(A):
    n = len(A)
    for i=1 to n-1 do
        small = i
        for j=i+1 to n do 
            if a[j] < a[small] then
                j = s
        EXCHANGE A[s] with A[i]
'''
def selection_sort(a):
    n = len(a)
    for i in range(n-1):
        small = i
        for j in range(i+1,n):
            if a[j] < a[small]:
                j = small
        a[small], a[i] = a[i], a[small]