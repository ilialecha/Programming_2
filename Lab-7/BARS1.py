def bars(n):
    t=2
    for i in range( (2**n)-1 ):
        if i % 2 == 0:
            print("*")
        else:
            print("*"(ord(n)+1))

bars(3)
