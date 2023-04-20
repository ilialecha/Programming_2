import sys
seq=sys.stdin.readline().strip()

l1=[]

for x in seq:
	l1.append(x)
			
pre = ""

for x in range(len(l1)-2):
	if l1[x] == "A" and l1[x+1] == "T" and l1[x+2] == "G":
		
		pre = l1[x:len(l1)]
		pre = "".join(pre)
		l2 = []
		
		for x in range(0,len(pre),3):
			l2.append(pre[x:x+3])
		
		res=""
		
		for x in l2:
			if x=="TAA" or x=="TAG" or x=="TGA":
				res+=x
				print(res)
				break
					
			else:
				res+=x

