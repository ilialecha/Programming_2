from math import factorial
from easyinput import read_line
'''
function e_approximation(int i):
    if i==1 then
        return 0
    else:
        return i / factorial(i) + e_approx(i-1)
'''



def e_approx(i):
    if not i: return 0
    else:
        return i/factorial(i) + e_approx(i-1)

num = read_line()
while num  != "":
    num = int(num)
    res = "{:.10f}".format(e_approx(num))
    print(f"With {num} term(s) we get {res}.")
    num = int(read_line())