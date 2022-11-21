def sum_line(l):

    if len(l) == 0: return 0 
    return int(l[0]) + sum_line(l[1:])


print(sum_line([1,2,3,4,5]))