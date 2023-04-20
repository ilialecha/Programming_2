from jutge import read, read_line

"""
WORD_1(n, A)
	let L be an empty list
	insert an empty string to L
	
	sortA
	
	for i = 1 to n do
		let L' be an empty list
		
		for all w in L do
			for all x in A do
				w' = x,w
				
				append w' to L'
		
		L = L'
	
	return L
"""

n = read(int)
A = read_line().split()

def word_1(n, A):
	
	l = [""]
	A.sort()
	for i in range(0,n):
		l2 = []
		for w in l:
			for x in A:
				new_w = x+w
				l2.append(new_w)
		
		l = l2

	
	
	return l
	
	
for x in word_1(n, A):
	print(x)
	

	

