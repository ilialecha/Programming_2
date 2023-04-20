"""
BINARY-SEARCH(A, x)
	return BINARY-SEARCH(A, x, l, |A|)


BINARY-SEARCH(A, x, l, r)
	if ell > r then
		return -1
		
	else
		m = (ell + r) / 2
			
		else if x < A[m] then
			return BINARY-SEARCH(A, x, ell, m-1)
		
		else if x > A[m] then
			return BINARY-SEARCH(A, x, m+1, r)
		
		else
			return m
"""

def binary_search(A, x):
	return binary_search_rec(A, x , 0, len(A)-1)
	
def binary_search_rec(A, x , ell, r):
	if ell > r:
		return -1
	
	else:
		m = (ell + r) // 2
		
		if x < A[m]:
			return binary_search_rec(A, x, ell, m-1)
		
		if x > A[m]:
			return binary_search_rec(A, x, m+1, r)
	
		else:
			return m
	
L = list(range(1,11))

print(binary_search(L, 4))
