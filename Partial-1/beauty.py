'''
function beauty(s)
    let D be an empty dictionary
    for i = 1 to |s| do
        x = s[i]
        if x in D then
            D[x] = D[x] + 1
        else
            D[x] = 1
    least = |s|
    most = 0
    for all x in D do
        if D[x] < least then
            least = D[x]
        if D[x] > most then
            most = D[x]
    return most − least
'''

def beauty(s):
    D = dict()
    for i in s:
        if i in D: D[i]+=1
        else: D[i]=1
    least = len(s)
    most = 0
    for k in D:
        if D[k] < least: least = D[k]
        if D[k] >  most: most = D[k]
    return most - least

print(beauty("abaabc"))