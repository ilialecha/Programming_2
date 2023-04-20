def palindrome(seq):
    D = {
        "A":"T",
        "C":"G",
        "T":"A",
        "G":"C"
    }
    if seq == "": return True
    if len(seq) % 2 != 0: return False
    for i in range(len(seq)//2):
        if D[seq[i]] != seq[len(seq)-i-1]:
            return False
    return True

'''
function longest_palindrome_of( sequence )
    Let n = |sequence|
    Let L be an empty set(of strings)
    let max_len = 0 
    for i = 1 up to n-2 do                  # n-2 because j will be i + 2
        for j = i up to n by step 2 do      # Step 2 to be sure of only work with even length words.
            if j - i >= max_len then        # Because I uknown how exactly is assumed Palindrome function programmed. 
                if PALINDROME ( sequence[i : j+1] ) then
                    if j - i == max_len then
                        Add sequence[i : j] to L
                    else:
                        Let L be an empty set(of strings)
                        Add sequence[i:j] to L
    return L

'''
def longest_palindromes(sequence):
    n = len ( sequence )
    L = set()
    max_len = 0
    for i in range(n-2):
        for j in range(i+2,n,2):
            if j - i >= max_len:
                if palindrome(sequence[i:j]):
                    if j - i == max_len: L.add(sequence[i:j])
                    else:
                        max_len = j - i
                        L = {sequence[i:j]}
    return L

print(longest_palindromes("ACCTAGGTGAATTCAGCTTCGAGAATTC"))
