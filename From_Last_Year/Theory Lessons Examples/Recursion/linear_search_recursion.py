"""
LINEAR-SEARCH(A, x)
	return LINEAR-SEARCH(A, x, l, |A|)


LINEAR-SEARCH(A, x, l, r)
	if ell > r then
		return -1
		
	else if A[ell] == x then
		return ell
	else
		return LINEAR-SEARCH(A, x, ell+1, r)
"""

def linear_search(A, x):
	return linear_search_rec(A, x , 0, len(A)-1)
	
def linear_search_rec(A, x , ell, r):
	if ell > r:
		return -1
	
	elif A[ell] == x:
		return ell
		
	else:
		return linear_search_rec(A, x , ell+1, r)
	
L = list(range(1,11))

print(linear_search(L, 4))
