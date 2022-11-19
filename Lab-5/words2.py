import sys

def words(n,a):
    a.sort()
    L = []
    if n == 0: L.append("")
    else:
        W = words(n-1,a)
        for w in W:
            for x in a: L.append(w+x)
    return L 

n = int(sys.stdin.readline().strip())
a = sys.stdin.readline().strip().split()
words_ = words(n, a)

for w_ in words_: print(w_)
