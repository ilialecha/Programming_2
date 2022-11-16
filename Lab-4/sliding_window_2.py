from easyinput import read_line,read

'''
Pseudocode

function sliding_window_2(s,x,y):
    if |s| > x then
        Let L be an empty list
        L.append(s[0:x]) + sliding_window(s[y+1 : |s|],x,y)
    else
        return an empty list
'''

def sliding_window_2(s,x,y):
    if len(s) >= x:
        L=[]
        return[s[0:x]] + sliding_window_2(s[y:],x,y)
    else:
        return []

s = read(str)
x = read(int)
y = read(int)

[print(s) for s in sliding_window_2(s,x,y)]
