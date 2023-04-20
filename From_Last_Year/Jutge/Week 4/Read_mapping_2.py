import sys
"""
BUBBLE_SORT(A)
let A be an array with each value being each suffix with its position
	for i = 1 to |A| - 1 do 
		for j = |A| downto i + 1 --- 
			if A[j] > A[j+1] then 
				exchange A[j] with A[j+1] 
																							
"""
		
seq = sys.stdin.readline().strip()

l = []

for i in range(len(seq)):
	l.append([seq[i:],i+1])

for i in range(len(l)):
	
	for j in range(0, len(l)-1-i):
		
		if l[j] > l[j+1]:
			l[j], l[j+1] = l[j+1], l[j]
			

for x in l:
	print(x[1])

			

