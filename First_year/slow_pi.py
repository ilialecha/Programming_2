def slow_pi(i):
    if i == 0: return 4*(((-1)**i) / (2*i+1))
    else: return (((-1)**i) / (2*i+1)) + slow_pi(i-1)

def slow_pi1(a):

	total = 0

	for i in range(0,a+1):
		total += (((-1)**i) / (2*i+1))
		
	return round(total * 4.0, 4)
print(slow_pi(10))