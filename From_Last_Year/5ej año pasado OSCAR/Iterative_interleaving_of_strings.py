def interleaving(x,y):
	
	res = ""
	
	i = 0
	
	while i<len(x) and i<len(y):
		res += x[i] + y[i]
		
		i += 1
	
	res += x[i:] + y[i:]
	
	return res
	
	
print(interleaving("ab", "xyz"))
