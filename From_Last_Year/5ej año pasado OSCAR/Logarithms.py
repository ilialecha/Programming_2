from jutge import read

def myLog(b, x):
    if x < b:
        return 0  
    return 1 + myLog(b, x/b)

b, x = read(int,int)

while b is not None:

	print(myLog(b,x))

	b, x = read(int,int)
