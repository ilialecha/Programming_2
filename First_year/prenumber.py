
def pre_number_list(n,L):
    ant = ""
    LL=[]
    i=0
    while i <= len(L)-1 and n in L:
        if L[i] == n and ant !=  "": LL.append(ant)
        ant = L[i] ; i += 1
    return LL
