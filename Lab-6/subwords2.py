'''
function SUBWORDS(s):
    let S1, S2 = SUBWORDS(s,1)
    let L be an empty list(of strings)
    for all w € S2 do
        append w to L
    sort L
    return L

function SUBWORDS(s,i):
    if i > |s| then
        return 0, 0
    else
        S1,S2 = SUBWORDS(s,i+1)
        insert empty string to S1
        let S'1 be an empty set(of strings)
        for all w € S1 do
            let w' be the concatenation of s[i] and w 
            insert w' to S'1
            insert w' to S2
        return S1, S2
'''
import sys
def subwords ( s ):
    S1 , S2 = subwords_rec (s , 0)
    return sorted ([ x for x in S2 if len ( x ) != 0])
    
def subwords_rec (s , i ):
    if i == len ( s ):
        return set () , set ()
    else :
        S1 , S2 = subwords_rec (s , i + 1)
        S1 . add ('')
        SS1 = set ()
        for w in S1 :
            ww = s [ i ] + w
            SS1 . add ( ww )
            S2 . add ( ww )
        return SS1 , S2
s = sys . stdin . readline (). strip ()
for w in subwords ( s ):
    print( w )