def replacement(L,LL):
    if not 0 in L or len(LL) == 0:return L

    i,ii = 0,0
    Ll = []
    while i < len(L) and 0 in L[i:] and ii < len(LL):
        if L[i] == 0:
            Ll.append(LL[ii])
            ii+=1
        else: Ll.append(L[i])
        i+=1
    return Ll

def last(L,l):
    if L[0] == l: return -1
    else: return 1 + last(L[1:],l)

def replacement2(f,g):
    i,ii=0,0
    ff = []
    while i < len( f[:last(0)] ) and ii < len(g):
        if f[0] == 0:
            ff.append(g[ii])
            ii+=1
        else:
            ff.append(f[i])
        i+=1
    return ff.append([i for i in f[last(0)]])

L,LL = [1, -1, 0, 2, 0], [3, -2, 1]



print(replacement2(L,LL))