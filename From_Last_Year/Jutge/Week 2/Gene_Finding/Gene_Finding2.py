import sys

#GGTTTCTATGTGGCTAAATACGTTAACAAAAAGTCAGATATGGACCTTGCTGCTAAAGGTCTAGGAGCTAAAGAATGGAA
"""
PSEUDOCODE:

it <- 0
each3 <- 0

start <- False
end <- False

res <- ""

line <- readline

for x in line do
	it += 1
	
	for i =0 to |x| do
		if x[i] == "A" and x[i+1]== "T" and x[i+2] == "G" and start == False then
			res += x[i:i+3]
			it= i+3
			start = True
	
	while start and end == False do
		for i =0 to |x| do
			if (x[it]=="T" and x[it+1]=="A" and x[it+2]=="G") or (x[it]=="T" and x[it+1]=="A" and x[it+2]=="A") or (x[it]=="T" and x[it+1]=="G" and x[it+2]=="A") then
				res+=x[it:it+3]
				print(res)
				end <- True
				break
				
"""
it = 0
each3 = 0

res = ""

start = False
end = False

line = sys.stdin.readline().strip().split()
	
for x in line:
	it+=1
	
	for i in range(len(x)-2):
		
		if x[i] == "A" and x[i+1]== "T" and x[i+2] == "G" and start == False:
			
			res += x[i:i+3]
			it= i+3
			start = True
			

		
	while start and end == False:
		
		for i in range(it,len(x)-2):
			
			if (x[it]=="T" and x[it+1]=="A" and x[it+2]=="G") or (x[it]=="T" and x[it+1]=="A" and x[it+2]=="A") or (x[it]=="T" and x[it+1]=="G" and x[it+2]=="A"):
				res+=x[it:it+3]
				print(res)
				end = True
				break
				
			else:
				res+=x[i]
				each3+=1
													
				if each3%3==0:
					it+=3
					
		if end == False:
			break
	
