import sys

"""
GENE_FINIDING PSEUDOCODE:

searching_start <- True
end_found <- False

res = ""

i <- 0

while searching_start  and i < |seq|-3 do
	if seq[i:i+3] == "ATG" then
		res += seq[i:i+3]
		searching_start <- False
		i+=2
	i+=1
	
while searching_start is False and i < |seq|-3 do
	res += seq[i:i+3]
	
	if seq[i:i+3] == "TAA" or "TAG" or "TGA" then
		found_end <- True
		break
	i+=3

if found_end then
	return res

else:
	return nil
"""

#TAA, TAG, or TGA.

#input: GGTTTCTATGTGGCTAAATACGTTAACAAAAAGTCAGATATGGACCTTGCTGCTAAAGGTCTAGGAGCTAAAGAATGGAA

searching_start = True
found_end = False

seq=sys.stdin.readline().strip()

res = ""

i = 0

while searching_start and i < len(seq)-2:
	if seq[i] == "A" and seq[i+1]=="T" and seq[i+2]=="G":
		res += seq[i:i+3]
		searching_start = False
		
		i += 2
		
	i+=1

while searching_start == False and i < len(seq):
	
	res += seq[i:i+3]
	
	if (seq[i]=="T" and seq[i+1]=="A" and seq[i+2]=="G") or (seq[i]=="T" and seq[i+1]=="A" and seq[i+2]=="A") or (seq[i]=="T" and seq[i+1]=="G" and seq[i+2]=="A"):

		found_end = True
		break
	
	i+=3
	
#input: GGTTTCTATGTGGCTAAATACGTTAACAAAAAGTCAGATATGGACCTTGCTGCTAAAGGTCTAGGAGCTAAAGAATGGAA

#if found_end:
print(res)
#else:
	#print(None)




		
