from easyinput import read_line
def parenthesis(line):
    clean = 0 ; opened = False
    for i in range(len(line)-1):
        if line[i] == "(" and opened == False and line[i+1] != "(":
            for j in range(i+1,len(line)):
                if line[j] == "(":
                    opened = False
                    break
                else:
                    if line[j] == ")":
                        clean+=1
                        opened = False
                        break
    return clean

line = read_line()
lines = 1
while line is not None:
    t = parenthesis(line)
    if t > 0:print(f"Line {lines} contains {t} regions.")
    line = read_line()
    lines +=1
