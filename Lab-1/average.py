from sys import stdin
'''
procedure average(L)
    let n be |L|
    let r be an integer
    for i=1 up to n do
        r = r + L[i]
    output r/n

'''
def average(l):
    l = l.split()
    n = len(l)
    r = 0
    for i in range(n):
        r += int(l[i])
    print("%.2f"%(r/n))

average("1 2 3 4 5 6 7 8 9 10")

def average2(s):
    print( "%.2f" % (( sum( float(i) for i in s.split() ) )/len(s.split())) )
