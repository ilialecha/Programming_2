def gcd(a,b):
	
	if a==0:
		return b
	
	elif b == 0:
		return a
	
	while a != b:
		
		if a > b:
			a = a-b
			
		else:
			b = b-a
		
	return	a
		

print(gcd(0,70))
	
