from easyinput import read
D = dict()
n = read(int)
r = 0
for i in range(n):
    nn = read(int)
    if nn in D:
        if i == n-1: r = D[nn]
        else: D[nn]+=1
    else: D[nn]=1
print(r)
