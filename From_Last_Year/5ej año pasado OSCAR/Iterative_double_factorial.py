def double_factorial(n):
	
	if n == 0:
		return 1
	
	else:
		r = 1
		for i in range(n, -1, -2):
			if i>0:
				r = r*i
		
		return r
			
		
print(double_factorial(6))
		
