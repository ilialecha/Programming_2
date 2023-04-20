from jutge import read, read_line

"""
WORD2(n, A)
	let L be an empty list
	insert an empty string to L
	
	sort A
	
	C = 0
	
	return WORD2_REC(n, A, L, C)
	
WORD2_REC(n, A, L, C)
	let L' be an empty list
	
	for all w in l do
		for all x in A do
			w' = w,x
			
			append w' to L'
	L = L'
	C += 1
	
	if C != n then
		return WORD2_REC(n, A, L, C)
		
	return L
"""


n =read(int)
A = read_line().split()

def word2(n, A):
	
	l = [""]
	A.sort()
	count = 0
	
	return word2_rec(n, A, l, count)


def word2_rec(n, A, l, count): 
	
	l2=[]
	
	for w in l:
		for x in A:
			new_w = x+w
			l2.append(new_w)
	
	l = l2
	count += 1
	
	if count!=n:
		return word2_rec(n, A, l, count)
			
	return l
	

for x in word2(n, A):
	print(x)

