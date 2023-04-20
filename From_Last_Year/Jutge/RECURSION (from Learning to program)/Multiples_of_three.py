def sum_of_digits(n):
	
	s = 0
	
	if n != 0:
		
		s = (n%10) + sum_of_digits(n//10)
		
		
	
	return s

def is_multiple_3(n):
	
	num = sum_of_digits(n)
	
	if num%3 == 0:
		return True
	
	else:
		return False






