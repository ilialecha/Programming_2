import sys

"""
RNA_TO_PROTEIN(S)
	let protein_dict be a dictionary/map with all possible RNA codons as key and the pretein as value
	while i < |S| and not searching_start do
		if codon = "AUG" then
		searching_start <- True
		
	while i < |S| and searching_start do
		if codon = "UAA" or "UAG" or "UGA" then
			searching_end <- True
			break
			
		else res <- protein_dict[codon]
	
	if searching_start and searching_end then
		print res
"""

#GUCGCCAUGAUGGUGGUUAUUAUACCGUCAAGGACUGUGUGACUA

seq = sys.stdin.readline().strip()

res = ""
i = 0

start = False
end = False

dic = {
        'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
        'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'UGU':'S', 'AGA':'R', 'AGG':'R',                
        'CUA':'L', 'CTC':'L', 'CUG':'L', 'CUU':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
        'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
        'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
        'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
        'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
        'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
        'UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'_',
        'UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W',
    }

while i <= len(seq)-3 and start == False:
	
	if seq[i:i+3] == "AUG":
		start = True
		i+=2
	
	i+=1

while i <= len(seq)-3 and start == True:
	
	if seq[i:i+3] == "UAA" or seq[i:i+3] == "UAG" or seq[i:i+3] == "UGA":
		end = True
		break
	
	else:	
		
		res += dic[seq[i:i+3]]
	
	i+=3

if start and end:
	print(res)

#GUCGCCAUGAUGGUGGUUAUUAUACCGUCAAGGACUGUGUGACUA

	

