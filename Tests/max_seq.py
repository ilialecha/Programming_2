from easyinput import read, read_line

a,b,n = read(int),read(int),read(int)

fa, fb, finish = False, False, False
section = list()

while n is not None and not finish:
    if not fa and not fb and n==a:
        fa = True
    elif fa and not fb and n!=b:
        section.append(n)
    elif fa and not fb and n==b:
        finish = True
    n = read(int)

if finish and len(section) != 0: print("maximum is: ",sorted(section)[-1])
elif finish and len(section) == 0: print("empty section")
else: print("nonexistent section")