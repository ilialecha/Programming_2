'''
Pseudocode

def Subwords(s)
	if len(s) == 1 then
		return [s]
	else if len(s)==0 then
		return []
	else
		l = Subwords(s[1:])
		for i=0 to i=|s| do
			append s[0:i+1] to l
		
		return l

l =set(Subwords(s))

let l2 be an empty list
for all x in l do
	append x to l2

sort l2

for all x in l2 do
	output x
'''

import sys

def Subwords(s):
	if len(s)==1:
		return [s]
	
	elif len(s)==0:
		return []
		
	else:
		l = Subwords(s[1:])
		for i in range(0, len(s)):
			l.append(s[0:i+1])
		return l
	
s = sys.stdin.readline().strip()
l = set(Subwords(s))

l2 =[]
for x in l:
	l2.append(x)
l2.sort()

for x in l2:
	print(x)


		
		
		
			
	
	












	
	
		
	
	
