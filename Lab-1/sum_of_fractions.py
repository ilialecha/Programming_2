from easyinput import read_line

'''
function sum_of_frac(a,b,k)
    Let i = 0 
    Let r = 0
    while (a+(i*k)) < b DO
        r = r + 1/(a+(i*k))
    return r
'''

def sumFrac(a,b,k):
    i=0
    op=0
    while a+(i*k) <= b:
        op += 1/(a+(i*k))
        i+=1
    print("%.4f" % op)

triplet =read_line()

while triplet != "":
    sumFrac(int(triplet.split(" ")[0]),
    int(triplet.split(" ")[1]),
    int(triplet.split(" ")[2]))
    triplet =read_line()


