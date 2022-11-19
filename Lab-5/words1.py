import sys
def words (n , a ):
    a . sort ()
    L = [""]
    for i in range ( n ):
        LL = []
        for w in L :
            for x in a :
                LL += [ w + x ]
        L = LL
    return L
n = int ( sys . stdin . readline (). strip ())

a = sys . stdin . readline (). strip (). split ()
for w in words (n , a ):
    print ( w )