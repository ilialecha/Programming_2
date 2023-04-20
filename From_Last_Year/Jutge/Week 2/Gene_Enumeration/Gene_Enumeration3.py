import sys

"""
PSEUDOCODE:

prep = ""

for x = 0 to |seq| do
	if seq[x]=="A" and seq[x+1]=="T" and seq[x+2]=="G" then
		prep = seq[x:|seq|]
		
		res = ""
		
		for for i = 0 to |seq| in intervals of 3 do
			if prep[i:i+3]=="TAA" or prep[i:i+3]=="TAG" or prep[i:i+3]=="TGA" then
				res+=prep[i:i+3]
				print(res)
				break
			
			else then
				res+=prep[i:i+3]

"""

seq=sys.stdin.readline().strip()

prep = ""

for x in range(len(seq)-2):
	
	if  seq[x]=="A" and seq[x+1]=="T" and seq[x+2]=="G":
		prep = seq[x:len(seq)]
		
		res = ""
		
		for i in range(0, len(prep), 3):
			if prep[i:i+3]=="TAA" or prep[i:i+3]=="TAG" or prep[i:i+3]=="TGA":
				res+=prep[i:i+3]
				print(res)
				break
			
			else:
				res+=prep[i:i+3]
		
		
				
