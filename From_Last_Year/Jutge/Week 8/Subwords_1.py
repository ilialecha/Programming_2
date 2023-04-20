import sys

"""
SUBWORDS(s)
	let S be an empty set (of strings)
	
	for i = 1 to |s| do
		for j = 1 to |s| do
			insert s[i,.......,j] in S
	
	let L be an empty list (of strings)
	
	for all w in S do
		append w to L
	
	sort L
	return L
	
"""
s = sys.stdin.readline().strip()

def subwords(s):
	S = set()
	for i in range(len(s)):
		for j in range(i,len(s)):
			S.add(s[i:j+1])
			print(S)
	
	l = []
	
	for x in S:
		l.append(x)
	
	l.sort()
	
	return l			

for x in subwords(s):
	print(x)
