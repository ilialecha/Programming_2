'''
function LCLIST(L)
    let L' be an empty list(of strings)
    let ADD be True
    for all l € L do
        for all l' € l do
            if l' is upper then
                add = False
                break loop
        if add = True then
            append l to L'
        add = True
    sort L'
    return L'
'''
def lclist(L):
    LL = []
    add = True
    for l in L:
        for ll in l:
            if ll.isupper():
                add = False
                break
        if add: LL.append(l)
        add = True
    return sorted(LL)





print(lclist(['En', 'un', 'lugar', 'de', 'La', 'Mancha']))