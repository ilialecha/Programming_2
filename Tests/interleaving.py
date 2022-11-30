from easyinput import read

def interleaving_(number1,number2):
    interleaving = 0
    exponent = 0
    while number1 > 0 or number2 > 0:
        interleaving += (number2 % 10) * (10**exponent)
        exponent += 1
        interleaving += (number1 % 10) * (10**exponent)
        exponent +=1

        number1 //= 10
        number2 //= 10
    return interleaving

'''x,y = read(int),read(int)
while x is not None and y is not None:
    print(interleaving_(x,y))
    x,y = read(int),read(int)'''


def rec_interleaving(number1,number2,exponent):
    if number1 == 0 and number2 == 0: return 0
    if exponent % 2 == 0:
        return (number2 % 10) * (10**exponent) + rec_interleaving( number1, number2//10, exponent+1 )
    if exponent % 2 != 0:
        return (number1 % 10) * (10**exponent) + rec_interleaving( number1//10, number2, exponent+1 )
#print(rec_interleaving(3,0,0))

