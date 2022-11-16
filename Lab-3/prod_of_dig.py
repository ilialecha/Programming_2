from easyinput import read


def prod_of_dig(string):
    tmp = 1
    if "0" in string: return print(f"The product of the digits of {string} is 0.")
    if len(string)==1: return print(f"The product of the digits of {string} is {string}.")
    while len(string)!=1:

        if "0" in string: return print(f"The product of the digits of {string} is 0.")
        if len(string)==1: return print(f"The product of the digits of {string} is {string}.")
        
        for s in string:
            tmp *=int(s)
        print(f"The product of the digits of {string} is {tmp}.")
        string,tmp=str(tmp),1

input = read()
while input is not None :
    prod_of_dig(input)
    print("----------")
    input = read()