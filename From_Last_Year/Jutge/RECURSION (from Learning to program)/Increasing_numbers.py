def is_increasing(n):
	
	if n<10:
		return True
		
	else:
		new = n//10
		
		if n%10 >= new%10:
			return is_increasing(new)
			
			
		else:
			return False
			

		
