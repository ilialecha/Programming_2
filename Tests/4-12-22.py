def is_gc_neutral2(DNA_Seq):
    n = len ( DNA_Seq )
    if n % 2 == 0:
        #Can be GC neutral
        return 2 * sum( [ 1  for nucleotide in DNA_Seq if nucleotide == 'C' or nucleotide == 'G' ] ) == n
    #Cannot be GC neutral:
    return False
#print(is_gc_neutral2("ACACAGAG"))

def R_is_gc_neutral( DNA_Seq, low, high):
    if low == high: return 0 
    return 1 + R_is_gc_neutral( DNA_Seq, low + 1, high ) if DNA_Seq[ low ] == 'G' or DNA_Seq[ low ] == 'C' else 0 + R_is_gc_neutral( DNA_Seq, low + 1, high )

def gc_neutral_base_case( DNA_Seq, size ):
    if size % 2 == 0: return 2 * R_is_gc_neutral( DNA_Seq, 0, size) == size
    return False
#print( gc_neutral_base_case( "AACC" ) )

def largest_gc_neutral_of( DNA_Seq ):
    n = len ( DNA_Seq )
    largest = 0
    for i in range( n - 1 ):
        for j in range( i , n ):
            # If finding LAST largest occurrence, check if j - i + 1 >= largest
            if gc_neutral_base_case( DNA_Seq[ i : j+1], j - i + 1 ) and  j - i + 1 > largest: 
                largest = j - i + 1
    return largest
#print(largest_gc_neutral_of("ACA"))
def longest_gc_neutral_of( DNA_Seq ):
    n = len ( DNA_Seq )
    l = 0
    longest = set()
    for i in range( n-1 ):
        for j in range ( i, n ):

            if gc_neutral_base_case( DNA_Seq[ i : j + 1 ], j - i + 1 ) and j - i + 1 >= l:
                if j-i+1 == l:
                    longest.add( DNA_Seq[ i : j + 1] )
                else:
                    #New longest size found, restart longest list.
                    longest = { DNA_Seq[ i : j + 1] }
                    l = j - i + 1
                
    return longest
#print( longest_gc_neutral_of( "ACACTAGAG" ) )

def REC_PALINDROME( seq, low, high, basepairs ):
    if low > high:                                                  # O(1)
        return True                                                 # O(1)
    if seq[ low ] == basepairs[ seq[ high ] ] :                     # O(1)
        return REC_PALINDROME( seq, low + 1, high - 1, basepairs )  # T(n-2)

def IS_PALINDROME(seq):
    N = len ( seq ) # O(1)
    if N == 0:      # O(1)
        return True # O(1)
    if N % 2 == 0:  # O(1)
                    # T(n) = T(n-2) + O(1) = O(n)
        return REC_PALINDROME( seq, 0, N - 1, {'A' : 'T','C' : 'G','T' : 'A','G' : 'C'} )
    return False

print( IS_PALINDROME( "TTAA" ) )



