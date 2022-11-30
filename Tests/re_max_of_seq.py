from easyinput import read,read_line
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

max_of_seq()