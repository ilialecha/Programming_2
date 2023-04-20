import sys
"""
SUBWORDS(s)
	S1, S2 = SUBWORDS_REC(s, 0)
	
	let L be an empty list (of strings)
	
	for all w in S2 do 
		append w to L
	
	sort L
	return L
	
SUBWORDS_REC(s, i)
	if i > |s| then
		return {}, {}
	
	else
		S1, S2 = SUBWORDS_REC(s, i+1)
		
		insert the empty string in S1
		
		for all w in S1 do
			for j = 1 to |s| do
				insert s[i,.......,j+1] in S2
	
	return S1, S2	
"""

def subwords(s):
		S1, S2 = subwords_rec(s, 0)
		
		l = []
	
		for w in S2:
			l.append(w)
		
		l.sort()
		
		return l

def subwords_rec(s, i):
	
	if i > len(s):
		return set(), set()
		
	else:
		
		S1, S2 = subwords_rec(s, i+1)
		
		S1.add("")
		
		for w in S1:
			for j in range(i,len(s)):
			
				S2.add(s[i:j+1])
			
	return S1, S2
	
s = sys.stdin.readline().strip()

for x in subwords(s):
	print(x)
