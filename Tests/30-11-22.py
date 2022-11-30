from easyinput import read,read_line
'''
    procedure interval(a, b):
        if i = b then
            output i AND new line
        else 
            output i WITH separator = ","
'''
def interval(a,b):
    for i in range(a,b+1):
        if i == b : print(i)
        else: print(i,end=",")
interval(15,21)
'''
    function interval_rec(a, b):
        if i = b then
            output i AND new line
        else 
            output a WITH separator = ","
            return interval_rec(a+1,b)
'''
def interval_rec(a,b):
    #Base case.
    if a == b :
        print(a)
    #Recursive case
    else:
        print(a,end=",")
        return interval_rec(a+1,b)
interval_rec(15,21)

def average():
    input = read(float)
    total = 0
    n = 0
    while input is not None:
        n+=1
        total+=input
        input = read(float)
    return "{:.2f}".format(total/n)
#print(average())

def average_rec(total,n):
    input = read(float)
    if input is None:
        return "{:.2f}".format(total/n)
    else:
        return average_rec(total+input,n+1)
#print(average_rec(0,0))

def sum_frac(a, b, k):
    total = 0.
    index = 0
    while a + (index*k) <= b:
        total += 1 / (a+(index*k))
        index+=1
    return "{:.4f}".format(total)

def sum_frac_rec(a, b, k, total, index):

    a,b,k = read(int),read(int),read(int)

    if a + (index*k) <= b:
        return sum_frac_rec(a,b,k, total+(1/(a + (index*k))),index+1)  
    return "{:.4f}".format(total)

'''a,b,k = read(int),read(int),read(int)
while a is not None:
    print(sum_frac_rec(a, b, k, 0., 0))
    a,b,k = read(int),read(int),read(int)'''

def complementary(S,D):
    return "".join([D[s] for s in S[::-1]])
def read_abund():
    D = {"A":"T","T":"A","C":"G","G":"C"}
    F = {}
    read = read_line()
    while read is not None:
        r = complementary(read,D)
        if r < read:
            read = r
        F[read] = F.get(read,0)+1        
        read = read_line()
    for k in sorted(F):
        print(f"{k} {F[k]}")
#read_abund()


def max_of_seq():
    n = read(int)
    max_ = None
    while n is not None:
        for i in range(n):
            inputint =  read(int)
            if max_ == None: max_ = inputint
            elif inputint > max_: max_=inputint
        print(max_)
        max_ = None
        n = read(int)

#max_of_seq()

def count_freq():
    D = {}
    for i in range(read(int)):
        x = read(int)
        D[x] = D.get(x,0)+1
    for k in sorted(D):
        print(f"{k} : {D[k]}")

#count_freq()

def factorial(n):
    if n <= 1: return 1
    return n * factorial(n-1)
def e(n):
    if n == 0: return 0.
    return (n / factorial(n)) + e(n-1)
#print("{:.10f}".format(e(20)))


def bubble_sort(unsorted):
    n = len(unsorted)
    for i in range(n-1):
        for j in range(n-i-1):
            if unsorted[j] > unsorted[j+1]:  unsorted[j], unsorted[j+1] = unsorted[j+1],unsorted[j]
    return unsorted

def read_mapping1(S):
    D = [S[i:] for i in range(len(S))]
    return [len(S) - len(d) + 1 for d in bubble_sort(D)]
#print(read_mapping1( "TATAAT" ))

def missing():
    n = read(int)
    L = [-1 for i in range(n)]
    for i in range(n-1):
        nn = read(int)
        L[nn-1] = nn
    return L.index(-1)+1

def missing2(n):
    total = ((n*n)+n) // 2
    for i in range(n-1):
        total -= read(int)
    return total
#print(missing2(5))

def interleaving(number1, number2):
    digits = len( str( number1 ) )
    max_exponent = (digits * 2)-1
    interleaving = 0
    for i in range( len( str( number1 ) ) ):
        for j in range( i, i+1 ):
            interleaving += ( number1 // 10**(digits-1-i) )*10**(max_exponent)
            max_exponent -=1
            number1 -= (number1 // 10**(digits-1-i))* 10**(digits-1-i)
            interleaving += ( number2 // 10**(digits-1-i) )*10**(max_exponent) 
            max_exponent -=1
            number2 -=   (number2 // 10**(digits-1-i))* 10**(digits-1-i)
    return interleaving

print(interleaving(312,435))