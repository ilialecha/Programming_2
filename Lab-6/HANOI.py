from easyinput import read
def HANOI(n,left,middle,right):
    if n > 0:
        HANOI(n-1, left, right, middle)
        print(left,"=>",right)
        HANOI(n-1, middle,left, right)



HANOI(read(int),'A','B','C')