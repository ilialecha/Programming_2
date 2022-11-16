from easyinput import read, read_line
'''
Pseudocode
'''

def words(n,bases):
    bases = sorted(bases.split(" "))
    words = 0
    while words < 4**n:
        tmp_word = ""
        while len(tmp_word) < n:
            i = 0
            while i < len(bases):

                tmp_word += bases[i]
        words +=1

words(read(int),read_line())