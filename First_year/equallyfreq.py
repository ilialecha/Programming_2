from easyinput import read_line

line = read_line() ; found = False
while line is not None:
    line_,D = line.split(),dict()
    for l in line_:
        if l in D: D[l]+=1
        else: D[l] = 1

    S = set()
    for v in D.values():S.add(v)
    if sum(S) != len(line_):
        print(f"Line: '{line}' has some equally frequent values")
        found = True ; break
    line = read_line()

if found == False:print("No line has equally frequent values")