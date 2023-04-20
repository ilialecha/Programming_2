
import sys
"""
WORDS2(n, A)
	let L be an empty list (of strings)
	insert an empty string in L
	
	sort A
	
	c = 0
	
	return WORD2_REC(n, A, L, c)
	
WORDS2_REC(n, A, L, c)
	let L' be an empty list(of strings)
	
	for all w in l do
		for all x in A do
			w' = w,x
			
			append w' to L'
	
	L = L'
	c += 1
	
	if C != n then
		return WORD2_REC(n, A, L, c)
		
	return L
"""

def words2(n, A):
	
	l = [""]
	
	A.sort()
	
	c = 0
	
	return words2_rec(n, A, l, c)

def words2_rec(n, A, l, c):
	
	l2 = []
	
	for w in l:
		for x in A:
			new = w+x
			l2.append(new)
	
	l = l2
	c += 1
	
	if c != n:
		
		return words2_rec(n, A, l, c)
	
	return l
	
n = int(sys.stdin.readline())

A = sys.stdin.readline().split()

for x in words2(n, A):
	print(x)

