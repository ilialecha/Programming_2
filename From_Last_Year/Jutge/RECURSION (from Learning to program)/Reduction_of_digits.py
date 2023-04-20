def reduction_of_digits(x):
	s = x
	
	if len(str(x)) != 1:
		
		s = 0
		
		for x in str(x):
			s += int(x)
			
	
		
		return(reduction_of_digits(s))
		
	
	else:
		return s
		
