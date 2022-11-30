from easyinput import read
def missing():
    n = read(int)
    while n is not None:
        L = [-1 for i in range(n)]
        for i in range(n-1):
            nn = read(int)
            L[nn-1] = nn
        print(L.index(-1)+1)
        n = read(int)
missing()