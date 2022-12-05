def is_prime(n):
    '''
    Requires a non negative integer n.
    Returns True when n is prime 
    Returns False when n is not prime
    '''
    if  n < 2:
        return False
    d = 2
    while d*d <= n:
        if n%d == 0:
            return False
        d += 1
    return True
def next_is_prime(num):
    return is_prime( num )
def ant_is_prime(num):
    return is_prime( num )
# Mal algoritmo no, lo siguiente. 
def has_prime_chain_( num_list, size ):
    N = len( num_list ) ; consecutive = 0 ; index = 0 ; start_index = -1
    while N-index+consecutive >= size and consecutive <= size and index <= N:
        num = num_list[index]
        if is_prime(num):
            if consecutive == 0: start_index = index
            if consecutive + 1 > size: 
                start_index = -1
                break
            consecutive += 1
            if consecutive == size:
                if ( 0 < index < N - 1 ) and not ant_is_prime(num_list[index-1]) and not next_is_prime(num_list[index+1]):
                    break
                elif index == N-1:
                    break
                elif index < N-1 and is_prime( num_list[index+1]) or is_prime( num_list[index-1] ):
                    consecutive = 0
                    start_index = -1
                else:
                    start_index = -1
        else:
            consecutive = 0
            start_index = -1
        index += 1
    return start_index

# Mal algoritmo no, lo siguiente pero un poco menos :):
def has_prime_chain__( num_list, size ):
    # As in sliding windows.
    index = 0
    N = len( num_list )
    start_index = -1
    chain = True
    while N - index >= size:
        sub = num_list[index : index+size]
        for num in sub:
            if not is_prime(num):
                chain=False
                break
        if chain: 
            start_index = index
            if index == 0 and (index + size) < N: #Está al principio
                if not next_is_prime( num_list[index+size]):
                    break #Found at the beggining.
            elif index > 0:
                if index + size < N: #Está en medio.
                    if not ant_is_prime( num_list[index-1]) and not next_is_prime( num_list[index+size] ):
                        break # Found in the middle
                if index + size == N: #Está al final
                    if not ant_is_prime( num_list[index-1]):
                        break #Found at the end.
        index +=1
        chain = True
        start_index = -1

    return start_index

#Este ya está un poco mejor.
#Judge no tiene en cuenta si el prime chain es en si toda la lista pasada y |num_list| = size.
def has_prime_chain( num_list, size ):
    start_index = -1 ; N = len ( num_list )
    # Only looping until num_list[i : ] < size
    for i in range( 0, N - size + 1 ):
        chain = True
        for j in range( i, i+size ):
            if not is_prime( num_list[j] ):
                chain = False
                break

        if chain: #All numbers within the interval are prime numbers.
            #The prime chain is at the beginning and may be the whole list :
            if i == 0 and ( (size < N and not next_is_prime( num_list[i+size])) or size == N ):
                start_index = i
                break #Found at the beggining.       
            elif i > 0:
                #The prime chain is on the middle:
                if i + size < N and not ant_is_prime( num_list[i-1]) and not next_is_prime( num_list[i+size] ): 
                    start_index = i
                    break # Found in the middle
                
                #The prime chain is on the end:
                if i + size == N and not ant_is_prime( num_list[i-1]):
                    start_index = i
                    break #Found at the end.       
    return start_index
'''has_prime_chain([6, 2, 3, 5, 2], 3)
has_prime_chain([6, 2, 3, 5, 2], 4)
has_prime_chain([1, 2, 3, 4, 5, 7, 11], 3)
has_prime_chain([2, 3, 4, 5, 6, 7], 1)
has_prime_chain([3,3,3,3,3], 5)'''



