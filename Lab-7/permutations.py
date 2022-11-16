import sys
def permutations(s):
    S = list(s)

    L = {""}

    while len(S) != 0:
        x = S.pop()
        LL = set()
        for w in L:
            for i in range(len(L)+1):
                LL.add(w[:i]+x+w[i:])
        L = LL
    return sorted(L)

s = sys.stdin.readline().split()

for w in permutations(s): print(w)