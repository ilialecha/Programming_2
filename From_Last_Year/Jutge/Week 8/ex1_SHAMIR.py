import sys

s = sys.stdin.readline().strip()
l = []

def Subwords(s):
	if len(s)==1:
		l.append(s)
		return l
		
	elif len(s)>1:
		p = s
		for i in range(0, len(p)):
			l.append(p[0:i+1])
			
		
		return Subwords(s[1:])
	
		
l = set(Subwords(s))

l2 = []

for x in l:
	l2.append(x)
	
l2.sort()
for x in l2:
	print(x)
