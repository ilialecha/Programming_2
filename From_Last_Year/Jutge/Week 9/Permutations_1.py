import sys

"""
PERMUTATIONS (s)
	let S be an empty stack (of characters)
	
	for i = 1 to |s| do
		push s[i] onto S
	
	let L be an empty set (of strings)
	insert an empty string in L
	
	while S is not empty do
		pop from S the top element x
		
		let L' be an empty set (of strings)
		
		for all w in L do
			for i = 1 to |w|+1 do
				insert w[1,...,i-1] + x + w[i,...,|w|]
				
		L = L'
		
		let A be an empty list (of strings)
		
		for all w in L do
			append w to A
		
		sort A
		
		return A
"""

def permutations(s):
	S = []
	
	for i in range(len(s)):
		S.append(s[i])
	
	l = set()
	l.add("")
	
	while len(S) > 0:
		
		x = S.pop()
		
		l2 = set()
		
		for w in l:
			for i in range(len(w)+1):
				l2.add(w[:i] + x + w[i:])
		
		l = l2
		
	A = []
	
	for w in l:
		A.append(w)


	A.sort()
	
	return A


s = sys.stdin.readline().strip()

for x in permutations(s):
	print(x)
