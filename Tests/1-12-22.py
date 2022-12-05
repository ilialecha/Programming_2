from easyinput import read,read_line
def sliding_window( seq, size, step ):
    for i in range( 0, len(seq) - size + 1, step ):
        print( seq[ i: i + size ] )
#sliding_window("ACGGTAGACCT",5,2)
def recursive_sliding_window( seq, low, size, step ):
    if  len( seq[low:] ) - size > 0:
        print( seq[ low : low + size ] )
        return recursive_sliding_window( seq, low+step, size, step )
    return
#recursive_sliding_window( "ACGGTAGACCT", 0, 3, 1 )
def gcd(numA, numB):
    if numA == 0: return numB
    if numB == 0: return numA
    return gcd(numB, numA % numB)

def sum_of_digits( num ):
    if num <= 9: return num
    return ( num % 10 ) + sum_of_digits(num//10)
def is_multiple_3( num ):
    return sum_of_digits( num ) % 3 == 0

#print(is_multiple_3(8472))

def reverse_list_1(prev):
    input = read_line()
    if input != "end":
        print(reverse_list_1(input))
        return  prev
    return prev

reverse_list_1("")
    