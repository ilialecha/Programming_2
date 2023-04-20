"""
FACTORIAL(n)
	
	if n < 2 then 
		return 1
	
	else
		return n * factorial(n-1)

"""

def factorial_rec(n):
	
	if n < 2:
		return 1
	
	else:
		return n * factorial_rec(n-1)
	
	

print(factorial_rec(5))
