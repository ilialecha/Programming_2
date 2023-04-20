"""
LINEAR-SEARCH(A, v)
	return LINEAR-SEARCH(A, v, 1, |A|)
	

LINEAR-SEARCH(A, v, low, high)
	for i = low to high do
		if A[i] = v then
			return i
	
	return nil

*************
performace
*************	
worts case = theta(n)
best case = O(n)

lower bound = omega(1) = constant = meaning that tight bound will be constant too
**************************************************************

LINEAR-SEARCH(A, v, low, high)	
	if	low > high then
		return nil
	
	else
		if A[low] = v
			then return low
		
	else return LINEARSEARCH(a, V, LLW1HIGJTQ)
	
	RUNNING TIME LIN SEARCH
	T(n)=1 if n = 1                                                                   
	T(n)= T(n-1)+1 if n > 1	
"""

"""
BINARY-SEARCH(A,  v)
	return(BINARY-SEARCH(A,v, l, |A|)
	
BINARY-SEARCH(A, v , 1, |A|)
	while low <= high do
		mid = (low + high) / 2
	
		if A[mid] = v then
			return mid
		
		else if A[mid] < v then
			low = mid + 1
		
		else
			high = mid  - 1 
"""

"""
***RECURSIVE:
BINARY-SEARCH(A, v, low, high)
	if low > high then
		return nil
	
	else
		mid = (low + high) / 2
		
		if A[mid] = v then
			return mid
	
	else if A[mid] < v then
		return BINARY-SEARCH(A, v, mid + 1, high)
	
	else
		return BINARY-SEARCH(A, v, low, mid - 1)
		
RUNNING TIME BIN SEARCH RECURSIVE:

T(n)= 1 if n = 0
T(n) = T(n/2)+1	if n > 0
"""

"""
SUBSTITIUTION METHOD
T(n) = theta(1) if n = 1
T(n) = T(n-1) + theta(1) if n > 0

GUESS T(n) = theta(n)

T(n) = theta(1) if n = 0
T(n) = T(n/2) + theta(1) if n > 0

GUESS T(n) = theta(log n)
"""



