from easyinput import read_line
import sys

def set_of_sets(lines):

    final = list()

    for line in lines:
        tmp = [i for i in sorted(line.split(" "),key=str)]
        if tmp not in final: final.append(tmp)

    for i in sorted(final,reverse=True,key=str):
        print(" ".join(e for e in i))


line = read_line()
lines=[]
while line != "":
    lines.append(line)
    line = read_line()

set_of_sets(lines)
#["1 2 3 4 5 6","6 4 2","9 5 4 0 2 1","0 1 2 5 6 7","9","8 7","4 2 6","7 8"]