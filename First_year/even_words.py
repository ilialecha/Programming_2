from easyinput import read
# As it reads, it processes the actual S and return 1 or 0 
# depending is the size is even or odd. And calls itself to
# read an process another word.
'''
function KEEP():
    let a string S be a stream input
    if S is not empty then     #If S is empty is the base case. 
        if |S| MOD 2 = 0 then  #Checking if the word is even or not.
            return 1 + KEEP()
        else
            return 0 + KEEP()
    else
        return 0 
'''
def keep():
    S = read()
    if S is not None:
        if len(S) % 2 == 0: return 1 + keep()
        return 0+keep()
    else: return 0 

print(keep())