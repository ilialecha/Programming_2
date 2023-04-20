def number_of_digits(n):
	
	c = 0
	
	while n != 0:
		
		n = n//10
		
		c+=1
	
	return c
	

print(number_of_digits(4))
