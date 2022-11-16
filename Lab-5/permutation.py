n = 2
a = ["A","C","T","G"]

a.sort()
L = [""]
for i in range(n):
    LL = []
    for Li in L:
        for x in a: LL += [x+Li]
    L = LL
print(L)