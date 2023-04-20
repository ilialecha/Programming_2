"""ITERATIVE 

PERMUTATIONS (s)
	let S be an empty stack (of characters)
	
	for i = 1 to |s| do
		push s[i] onto S
	
	let L be an empty set (of strings)
	insert an empty string in L
	
	while S is not empty do
		pop from S the top element x
		
		let L' be an empty set (of strings)
		
		for all w in L do
			for i = 1 to |w|+1 do
				insert w[1,...,i-1] + x + w[i,...,|w|]
				
		L = L'
		
		let A be an empty list (of strings)
		
		for all w in L do
			append w to A
		
		sort A
		
		return A
	
	
"""

"""RECURSIVE:

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
