'''
    PROCEDURE selection-sort(a):
        n = len(a)
        for i = 1 to n-1 do 
            small = i 
            for j = i + 1 to n :
                if a[j] < a[i] then
                    small = j 
            EXCHANGE a[small] with a[i]
'''

def selection_sort(arr):
    for i in range(0, len(arr)-1):
        small = i 
        for j in range(i+1,len(arr)):
            if arr[j] < arr[small]: small = j 
        arr[i],arr[small] = arr[small], arr[i]


arr = [9,8,7,6,5,4,3,2,1]

selection_sort(arr)

print(arr)