"""BUBBLE_SORT PSEUDOCODE:

BUBBLE_SORT(A)
	for i = 1 to |A| - 1 do --- O(n-1) * (n-i) time = O(n^2) time
		for j = |A| downto i + 1 --- repeated n-i times, cost O(n-i) time each
			if A[j] < A[j-1] then --- O(1) time
				exchange A[j] with A[j-1] ----- hacerlo asi en python: A[j], A[j-1] = A[j-1], A[j]
												|						en c++: usar swap(A[j], A[j-1])
												|
												|
												|
												|
												|--> cost O(1) time					
																		


running time 

"""
