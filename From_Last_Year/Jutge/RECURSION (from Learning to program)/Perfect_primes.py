def is_prime(num):
	if num > 1:

		for i in range(2, int(num/2)+1):
			
			if (num % i) == 0:
				return False
				break
		else:
			return True

	else:
		return False

def sum_of_digits(n):
	
	s = 0
	
	if n != 0:
		
		s = (n%10) + sum_of_digits(n//10)
		b = is_prime(s)
		
	
	return s
	
def is_perfect_prime(n):
	
	return is_prime(sum_of_digits(n))
	
print(sum_of_digits(156))

