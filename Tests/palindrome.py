import time
from Bio.Seq import Seq
def palindrome(s):

    n = len(s)
    
    if n%2 != 0: return False
   
    n-=1

    D = {"A":"T","T":"A","C":"G","G":"C"}

    for i in range( ((n)//2) + 1):
        if s[i] != D[s[n-i]]: return False
    return True
