from jutge import read

"""
READ_ABUNDANCE(S)
	if S not in dict and comp_rev(S) not in dict then
		dict[minimum of S and comp_rev(S)] = 1
	
	else dict[minimum of S and comp_rev(S)] += 1
"""

seq = read(str)

d2 = {}

def comp_rev(s):
	
	d = {"A": "T", "T": "A", "C": "G", "G": "C"}
	res = ""
	
	for x in s:
		res += d[x]
	
	return res[::-1]
	
#d2[min(seq, comp_rev(seq))] = 1

while seq is not None:
	
	if seq  not in d2 and comp_rev(seq) not in d2:
		#print("new")
		d2[min(seq, comp_rev(seq))] = 1
		#print(d2)
		
	else:
		d2[min(seq, comp_rev(seq))] += 1
		#print(d2)
		
	seq = read(str)
	
		
for x in sorted(d2):
	print(x, d2[x])	
	
	



	

