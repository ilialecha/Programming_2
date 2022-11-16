#s="ACCTAGGT"
s="AACTT"

def palindrome(s):
    D = {
    "A":"T",
    "T":"A",
    "G":"C",
    "C":"G"
    }
    n = len(s)
    for i in range((n//2)+1):
        if s[i] != D[s[n-i-1]]:return False
    return True


print(palindrome(s))