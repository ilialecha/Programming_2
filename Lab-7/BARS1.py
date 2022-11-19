def bars(n):
    t = 2 ; odds = 0
    for i in range( (2**n)-1 ):
        if i % 2 == 0:
            print("*")
        else:
            print("*"*t)

bars(5)
