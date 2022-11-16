'''                                               
function gene_enumeration(s)
    n = |s|
    i = 1
    while i + 2 <= n do
        if s[i,...,i+2] = ATG then
            j = i + 3
            while j + 2 <= n do
                if s[j,...,j+2] ∈ {TAA, TAG, TGA} then
                    print s[i:j+2]
                    break
                j = j + 3
        i = i + 1
    return an empty string

'''
import sys
def gene_enumeration(s):
    n = len(s)
    i = 0
    while i + 2 <= n:
        if s[i : i + 3] == 'ATG':
            j = i + 3
            while j + 2 <= n:
                if s[j : j + 3] in {'TAA', 'TAG', 'TGA'}:
                    print (s[i : j + 3])
                    break
                j = j + 3
        i = i+1
    return ''

line = sys.stdin.readline().strip()
if line:
    print(gene_enumeration(line), end='')
else:
    print('', end='')
