def permutations(s):
    S = list(s)

    L = set()
    L.add("")

    while len(S) != 0:
        x = S.pop()
        LL = list()
        for w in L:
            for i in range(L):
                LL.append(w[:i],x,w[i:])
        L = LL
    A = []
    for w in L: A.append(w)
    A.sort()
    return A
