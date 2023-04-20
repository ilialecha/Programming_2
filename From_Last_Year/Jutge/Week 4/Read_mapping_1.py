from jutge import read
import sys
"""
READ_MAPPING1(S)
	let d be empty dictionary
	for i = 0 to  |S| do
		d[S[i:]] <-  i+1
		for x in sorted(d) do
			print(d[x])
	
"""

seq = sys.stdin.readline().strip()

d = {}

for i in range(len(seq)):
	d[seq[i:]] = i+1
		
for x in sorted(d):
	print(d[x])
		

