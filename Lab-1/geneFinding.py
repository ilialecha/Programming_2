from easyinput import read_line

#GGTTTCTATGTGGCTAAATACGTTAACAAAAAGTCAGATATGGACCTTGCTGCTAAAGGTCTAGGAGCTAAAGAATGGAA

'''
function gene_finding(s)
    n = |s|
    i = 1
    while i+2 <= n do
        if s[i, ..., i + 2] = ATG then
            j = i+3
            while j+2 <= n do 
                if s[j : j + 2] € [TAA, TAG, TGA] then
                    return s[i : j + 2]
                j = j + 3
        i = i + 3
    return an empty string
'''



def gene_finding(s):
    i = 0
    while i+2 <= len(s):
        if s[i:i+3] == "ATG":
            j = i + 3
            while j+2 <= len(s):
                if s[j: j+3] in ["TAA", "TAG", "TGA"]:
                    return s[i: j+3]
                j += 3
        i += 1
    return ""

output = gene_finding(read_line())

if output != "" : print(output, end="\n")