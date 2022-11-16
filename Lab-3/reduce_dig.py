
'''
function reduction_of_digits(s)
    Let R = 0
    while |s| > 1 do
        for i=1 up to |s| do
            R = R + Integer value of s[i]
        s = r
        r = 0
    return s
'''

def reduction_of_digits(s): # min = zeta(1), max = zeta(n)
    r = 0
    while len(str(s)) > 1:
        for i in str(s): r += int(i)
        s = r
        r=0
    return s
