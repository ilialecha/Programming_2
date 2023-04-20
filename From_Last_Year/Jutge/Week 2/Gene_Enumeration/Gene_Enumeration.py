import sys
#GAGTTTTATCGCTTCCATGACGCAGAAGTTAACACTTTCGGATATTTCTGATGAGTCGAAAAATTATCTTGATAAAGCAGGAATTACTACTGCTTGTTTACGAATTAAATCGAAGTGGACTGCTGGCGGAAAATGAGAAAATTCGACCTATCCTTGCGCAGCTCGAGAAGCTCTTACTTTGCGACCTTTCGCCATCAACTAACGATTCTGTCAAAAACTGACGCGTTGGATGAGGAGAAGTGGCTTAATATGCTTGGCACGTTCGTCAAGGACTGGTTTAGATATGAGTCACATTTTGTTCATGGTAGAGATTCTCTTGTTGACATTTTAAAAGAGCGTGGATTACTATCTGAGTCCGATGCTGTTCAACCACTAATAGGTAAGAAATCATGAGTCAAGT

"""
GENE_ENUMERATION PSEUDOCODE:

def gene_find(seq):
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

i <- 0

while i < |seq| do
	if seq[i:i+3] == "ATG" THEN
		if gene_find(seq[i:|seq|]) is not nil then
			return gene_find(seq[i:|seq|])
	
	i+=1
"""

def gene_find(seq):
	
	searching_start = True
	found_end = False
	res = ""

	i = 0

	while searching_start and i < len(seq)-3:
		if seq[i:i+3] == "ATG":
			res += seq[i:i+3]
			searching_start = False
			
			i += 2
				
		i+=1

	while searching_start == False and i < len(seq)-3:
		
		res += seq[i:i+3]
		
		if seq[i:i+3] == "TAA" or seq[i:i+3] == "TAG" or seq[i:i+3] == "TGA":
			found_end = True
			break
		
		i+=3
	
	if found_end:
		return res
	else:
		return None
	
	
seq=sys.stdin.readline().strip()
	
i = 0

while i < len(seq):
	
	if seq[i:i+3] == "ATG":
		if gene_find(seq[i:len(seq)]) is not None:
			print(gene_find(seq[i:len(seq)]))
			
	i+=1

#input: GAGTTTTATCGCTTCCATGACGCAGAAGTTAACACTTTCGGATATTTCTGATGAGTCGAAAAATTATCTTGATAAAGCAGGAATTACTACTGCTTGTTTACGAATTAAATCGAAGTGGACTGCTGGCGGAAAATGAGAAAATTCGACCTATCCTTGCGCAGCTCGAGAAGCTCTTACTTTGCGACCTTTCGCCATCAACTAACGATTCTGTCAAAAACTGACGCGTTGGATGAGGAGAAGTGGCTTAATATGCTTGGCACGTTCGTCAAGGACTGGTTTAGATATGAGTCACATTTTGTTCATGGTAGAGATTCTCTTGTTGACATTTTAAAAGAGCGTGGATTACTATCTGAGTCCGATGCTGTTCAACCACTAATAGGTAAGAAATCATGAGTCAAGT


		
