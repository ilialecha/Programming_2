'''
function REC_PALINDROME(S,l)
    if |S| mod 2 != 0 then
        return False
    if l > |S|-l-1 then
        return True
    else
        if S[l] = COMPLEMENT( S[ |S|-l-1 ] ) then
            return REC_PALINDROME( S, l+1 )
        else
            return False
function COMPLEMENT(C)
    Let D be an empty dictionary
    Insert key 'A' with value 'T' into D
    Insert key 'T' with value 'A' into D
    Insert key 'C' with value 'G' into D
    Insert key 'G' with value 'C' into D
    return D[C]
'''
def COMPLEMENT(c):
    D = dict()
    D['A'] = 'T'
    D['T'] = 'A'
    D['C'] = 'G'
    D['G'] = 'C'
    return D[c]

def REC_PALINDROME(s,l):
    if len(s) % 2 != 0: # Checking if odd or even
        return False
    if l > len(s)-l-1: # Checking if there are more elements.
        return True
    if s[l] == COMPLEMENT(s[len(s)-l-1]):
        return REC_PALINDROME(s,l+1)
    return False

print(REC_PALINDROME("TTTAAFA",0))