from jutge import read

n = read(int)

def number_of_digits(n):
	
	if n<10:
		return 1
		
	else:
		return 1 + number_of_digits(n//10)
		

print(number_of_digits(n))
