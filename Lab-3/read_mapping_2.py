from calendar import c
from easyinput import read_line

'''
    Pseudocode:

    suffixes = dict()
    for i in |sequence|: suffixes[i] = sequence[i:]
    {print(k[0]) for k in sorted(suffixes.items(), key=lambda item: item[1])}


'''

def bubble_sort(unsorted,reverse):

    n = len(unsorted)
    if reverse: 
        for i in range(n-1):
            for j in range(n-1,i, -1):
                if unsorted[j] < unsorted[j-1]: 
                    #Don't need to create a tmp variable to exchange 2 values.
                    unsorted[j], unsorted[j-1] = unsorted[j-1],unsorted[j]
    else:
        for i in range(n-1):
            for j in range(n-1,i, -1):
                if unsorted[j] > unsorted[j-1]: 
                    #Don't need to create a tmp variable to exchange 2 values.
                    unsorted[j], unsorted[j-1] = unsorted[j-1],unsorted[j]
    return unsorted


def suffix_array(sequence):

    #suffixes = dict()
    suff = list()
    #suff_dup = list()
    
    for i in range(0, len(sequence)): suff.append(sequence[i:])
        #suff_dup.append(sequence[i:])
    
    suff_dup = suff.copy()

    suff = bubble_sort(suff, True)

    for i in range(0, len(sequence)): print(suff_dup.index(suff[i])+1)


suffix_array(read_line())