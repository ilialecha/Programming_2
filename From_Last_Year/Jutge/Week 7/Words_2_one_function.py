"""
WORD1_REC(L, A, n, C)
	let L' be an empty list
	
	for all w in l do
		for all x in A do
			w' = w,x
			
			append w' to L'
	
	if C != n then
		return WORD2_REC(n, A, L', C+1)
		
	return L
"""

from jutge import read, read_line

n =read(int)
A = read_line().split()
A = sorted(A)

l=[""]
count = 0

def word1_rec(n, A, l, count): 
	l2=[]
	for w in l:
		for x in A:
			new_w = x+w
			l2.append(new_w)
	
	l = l2
	count += 1
		
	if count!=n:
		return word1_rec(n, A, l, count)
			
	return l
	

for x in word1_rec(n, A, l, count):
	print(x)
