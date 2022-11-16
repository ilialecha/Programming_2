def beauty(s):
    #Store it because is cheaper than calling twice to obtain the len of s
    n = len(s)
    D = dict()
    #Processing input
    for i in range(n):
        if s[i] in D: D[s[i]]+=1
        else: D[s[i]] = 1
    #Obtaining maximum and minimum
    low = n 
    high = 0
    for k in D.keys():
        if  D[k] < low: low = D[k]
        if D[k] > high: high = D[k]
    return high-low

def sum_beauty(s):
    s="aabcb"
    n = len(s)
    r = 0
    for i in range(n):
        for j in range(n+1):
            if i<j: r += beauty(s[i:j])
    return r

print(beauty("aababc"))

print(sum_beauty(" "))