import sys

count1=0
count = 0

list1=[]

oursequence=""

startcodon=False
endcodon=False

for line in sys.stdin:
	line = line.strip()
	line=line.split()
	print(line)
	
	for x in line:
		count+=1
		
		for i in range(len(x)-2):
			if x[i]=="A" and x[i+1]=="T" and x[i+2]=="G" and not startcodon:
				
				list1.append(x[i:i+3])
				oursequence+=x[i:i+3]
				count=i+3
				startcodon = True
				
		if not startcodon:
			break
			
		while startcodon and not endcodon:
			for i in range(count,len(x)-2):
				if (x[count]=="T" and x[count+1]=="A" and x[count+2]=="G") or (x[count]=="T" and x[count+1]=="A" and x[count+2]=="A") or (x[count]=="T" and x[count+1]=="G" and x[count+2]=="A"):
					
					oursequence+=x[count:count+3]
					print(oursequence)
					endcodon = True
					break
					
				else:
					oursequence+=x[i]
					count1+=1
					
					if count1%3==0:
						count+=3
						
			if not endcodon:
				break
