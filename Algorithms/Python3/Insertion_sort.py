'''
    PROCEDURE insertion-sort(a):
        n = len(a)
        for i=2 to n do
            key = a[i]
            j = i - 1
            while j>=0 and a[j] > key do
                a[j+1] = a[j]
                j = j - 1 
            a[j+1] = key 
'''

def insertion_sort(a):
    for i in range(1,len(a)):
        k = a[i]
        j = i - 1
        while j >= 0 and a[j] > k:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = k

a = [4,3,2,1]

insertion_sort(a)

print(a)