"""
SUBSETS(S)
	let L be an empty set
	n = |S|
	
	if n = 0 then
		append an empty list to L
	
	else
		for all x in SUBSETS(S_2,...,S_n) do
			append S to L
			let Y be a copy of X
			append S_1 to Y
			
			append 	Y to L
		
	return L
			
"""

def subsets(S):
	L = []
	
	if len(S) == 0:
		L += [[]]
	
	else:
		for X in subsets(S[1:]): #subsets(S, i+1)
			L.append(X)
			L.append([S[0]] + X)
	return L
	

print(subsets("ABC"))

