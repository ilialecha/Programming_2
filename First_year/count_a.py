def count_a(s,c):
    i = 0
    a = 0
    found = False

    while i<len(s) and not found:
        t = s[i]
        if s[i] == c:
            found = True
            break
        if s[i] == 'a': a+=1
        i+=1
    if found:return a
    else: return -1
