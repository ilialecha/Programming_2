from easyinput import read_line
import sys

'''
function reverse-complement(s):
    let C be an empty dictionary
    C = { 'A' : 'T' , 'C' : 'G' , 'G' : 'C' , 'T' : 'A'}
    for i=1 to |s| do
        s[i] = C[ s[n-(i-1)] ]
    return s 

function read_abundance(seq):
    let d be a dictionary
    for character in char_sequence do 
        r = reverse_complement(character)
        if r < s:
            s = r
        d[s] = 1 if empty or d[s]+1 if not empty
    return d 
    
'''

'''
Function used to obtain the complementary sequence of a given sequence with alphabet {A;T;C;G}
This function shall run the sequence backwards in order to return the complementary base of each character.
'''
def reverse_complement(s):
    C = { 'A' : 'T' , 'C' : 'G' , 'G' : 'C' , 'T' : 'A'}
    s = ''.join([ C[x] for x in s [::-1]])
    return s



def read_abundance (seq):
    d = dict ()
    for s in seq:
        r = reverse_complement (s)
        if r < s :
            s = r
        d[s] = d.get(s,0) + 1
    return d

S = list ()
for line in sys.stdin.readlines():
    s = line.strip()
    S.append(s)

D = read_abundance(S)
for s in sorted(D):
    print (s,D[s])
