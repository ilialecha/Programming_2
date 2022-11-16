from easyinput import read
def maxofseq():
    to_read = read(int)
    m=0
    for _ in range(to_read):
        x = read(int)
        if x > m: m=x
    print(m)

maxofseq()