import sys

"""
PERMUTATIONS (s)
	L = PERMUTATIONS ("", s)
	
	let A be an empty list (of strings)
	
	for all w in L do
		append w to A
	
	sort A
	return A
	
	
PERMUTATIONS(prefix, s)
	let L be an empty set (of strings)
	
	if |s| = 0 then
		insert prefix in L
	
	else
		for i = 1 to |s| do 
			for all w in PERMUTATIONS(prefix + s[i], s[1,...,i-1] + s[i+1,...,|s|]) do
				insert w in L
	
	return L
"""

def permutations(s):
	
	l = permutations_rec("", s)
	
	A = []
	
	for w in l:
		A.append(w)
	
	A.sort()
	
	return A
	
def permutations_rec(prefix, s):
	
	L = set()
	
	if len(s) == 0:
		L.add(prefix)
	
	
	else:
		
		for i in range(len(s)):
			for w in permutations_rec(prefix + s[i], s[:i] + s[i+1:]):
				print(i, prefix + s[i], s[:i] + s[i+1:])
				print("w: ", w)
				L.add(w)
	
	print(L)			
	return L
	

s = sys.stdin.readline().strip()

for x in permutations(s):
	print(x)
	
print(s[:5] + s[5+1:])
	


	
	
	
	
	
