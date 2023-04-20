from jutge import read
"""
WORD_COMPOSITION(S, n)
	let d be an empty dictionary
	
	for i = 0 to |S| do
		
		substring <- seq[i...i+n]
		
		if substring not in d then
			if |substring| == n then
				d[substring] <- 1
		else 
			d[substring] += 1
		
	return d

"""

def word_composition(seq, n):
	
	d = {}
	
	for i in range(len(seq)):
		
		substr = seq[i:i+n]
		
		if substr not in d:
			
			if len(substr) == n:
				d[substr] = 1
			
		else:
			d[substr] += 1

	return d

seq = read(str)

n = read(int)

res = word_composition(seq, n)

for x in sorted(res):
	print(x, res[x])

