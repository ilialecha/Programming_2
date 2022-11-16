def gc_neutral(S):
    n = len(S)
    if n % 2 != 0: return False
    c = 0 
    for i in S:
        if i=='C' or i=='G': c+=1
    return c == n//2
def gc_neutral2(S):
    n = len(S)
    if n%2!=0:return False
    else: return rec_gc_content(S,0,n-1) == n // 2
def rec_gc_content(S,low,high):
    if low>high:return 0
    elif S[low] == 'C' or S[low]=='G':
        return 1 + rec_gc_content(S,low+1,high)
    else:
        return 0 + rec_gc_content(S,low+1,high)
def longest_gc_neutral(S):
    n = len(S) ; l = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if j-i+1 > l and gc_neutral2(S[i:j+1]): l = j-i+1
    return l
def longest_gc_neutral2(S):
    n = len(S) ; l = 0 ; L = []
    for i in range(n-1):
        for j in range(i+1,n):
            if j-i+1 >= l and gc_neutral2(S[i:j+1]):
                if j-i+1 == l: L.append(S[i:j+1])
                else: 
                    L = [S[i:j+1]]
                    l = j-i+1
    return L


# Executions
S = "CCAAGT"

print(gc_neutral(S))
print(gc_neutral2(S))
print(longest_gc_neutral(S))
print(longest_gc_neutral2(S))
