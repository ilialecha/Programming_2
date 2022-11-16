from re import I


def linear_search(a,x):
    i = 0
    while i <= len(a) and a[i] != x:
        i+=1
    if i > len(a): return "nil"
    return i 

def binary_search(a, lo, hi, x):
    while lo <= hi:
        mid = (lo + hi) // 2
        if x==a[mid]:return mid
        elif x > a[mid]: lo+=1
        else: hi-=1 

def bubble_sort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]

def insertion_sort(a):
    '''
        For de 1 a n
        key = a[i]
        j = i-1
        while j>0 and a[j] > key:
            a[j+1] = a[j]
            j -=1
        a[j+1] = key
    '''
    for i in range(1,len(a)):
        key = a[i]
        j = i-1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j-=1
        a[j+1] = key

def selection_sort(a):
    for i in range(len(a)-1):
        s = i
        for j in range(i+1,len(a)):
            if a[j] < a[s]: s = j 
        a[i],a[s] = a[s],a[i]



a = [1,2,3,4,5,6,7,8,9]
b = [9,8,7,6,5,4,3,2,1]

insertion_sort(b)
print(b)