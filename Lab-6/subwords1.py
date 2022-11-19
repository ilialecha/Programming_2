from easyinput import read_line
'''
    FUNCTION SUBWORDS(S):
        #Set for avoiding repeated subwords.
        Let W be an empty set(of strings)
        for i = 1 up to |S| do
            for j = i up to |S| do
                insert S[i:j] into W
        Let L be an empty list(of strings)
        for all w € W do:
            append w into L
        sort L
        return L
'''
def subwords(S):
    W = set()
    n = len(S)
    for i in range( n ):
        for j in range( i, n ): W.add(S[i:j+1])
    L = []
    for w in W: L.append(w)
    return sorted(L)
S = read_line()
[print(w) for w in subwords(S)]
