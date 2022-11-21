'''
function COMPLEMENTARY(s)
    let D be an empty dictionary
    insert D[A] = T to D
    insert D[T] = A to D
    insert D[C] = G to D
    insert D[G] = C to D
function PALINDROME(S)
    if |S| MOD 2 != 0 then
        return False
    else
        return REC_PALINDROME(S,1)
function REC_PALINDROME(S,l)
    if l >= |S| - l - 1 then 
        return True
    else
        if S[0] = COMPLEMENTARY(S[-1]) then
            return REC_PALINDROME(S[1:-1],0)
        else
            return False

'''
def COMPLEMENTARY(s):
    D = dict()
    D['A'],D['T'] = 'T','A'
    D['C'] = 'G'
    D['G'] = 'C'
    return D[s]

def rec_palindrome(S):
    if 0 >= len(S)-1:
        return True

    if S[0] == COMPLEMENTARY(S[len(S)-1]):
        return rec_palindrome(S[1:len(S)-1])
    return False

def palindrome(S):
    if len(S) % 2 != 0: return False
    return rec_palindrome(S)


print(palindrome("ACCTAGGT"))