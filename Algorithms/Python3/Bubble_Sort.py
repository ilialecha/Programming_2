'''
    PROCEDURE bubble-sort(a):
        n = len(a)
        for i=1 to n-1 do 
            for j=n down to i+1 do 
                if a[j] > a[j+1] then
                    EXCHANGE a[j] and a[j+1]

'''
def bubble_sort(unsorted):
    n = len(unsorted)
    for i in range(n-1):
        for j in range(n-i-1):
            if unsorted[j] > unsorted[j+1]:  unsorted[j], unsorted[j+1] = unsorted[j+1],unsorted[j]
    return unsorted

print(bubble_sort([5,4,3,1,2]))