from easyinput import read_line
def REVERSE(prev):
    s = read_line()
    if s is not None:
        print(REVERSE(s))
        return prev
    else:
        return prev

REVERSE("")