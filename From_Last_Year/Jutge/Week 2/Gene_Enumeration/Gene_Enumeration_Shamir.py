import sys
s=sys.stdin.readline().strip()


list1=[]
for x in s:
	list1.append(x)
			
oursequence=""
for x in range(len(list1)-2):
	if list1[x]=="A" and list1[x+1]=="T" and list1[x+2]=="G":
		oursequence=list1[x:len(list1)]
		oursequence=''.join(oursequence)
		list2=[]
		n=3
		for x in range(0,len(oursequence),n):
			list2.append(oursequence[x:x+n])
		#print(list2)
		
		finalsequence=""
		done = False
		for x in list2:
			if x=="TAA" or x=="TAG" or x=="TGA":
				finalsequence+=x
				print(finalsequence)
				break
				
				
			else:
				finalsequence+=x
