"""
WORD-COMPOSITION(s, k)
	
	n = |S|
	
	let D be an empty dicctionary (of strings to integers)
	
	for i = 1 to n-k+1 do
		w = s[i,...,i+k-1] is k-mer
		if w in D then
			D[w] = D[w] + 1
		
		else
			D[w] = 1
		
		sort D
		
		let L be an empty list (of pairs and string integer)
		
		for all w in D do
			append(W, D[w] to L)
		
		return L
"""
from jutge import read


def word_composition(seq, n):
	
	d = {}
	l = []
	
	for i in range(len(seq)-n+1):
		
		w = seq[i:i+n]
		
		if w not in d:
			
			#if len(w) == n:
				d[w] = 1
			
		else:
			d[w] += 1
	
	sorted(d)
	
	#return d
	
	for x in d:
		
		l.append((x, d[x]))
		
	return l



seq = read(str)

n = read(int)

res = word_composition(seq, n)

for x in res:
	print(x[0],x[1])

