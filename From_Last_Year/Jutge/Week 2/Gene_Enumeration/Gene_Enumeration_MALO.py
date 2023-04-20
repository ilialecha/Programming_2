from jutge import read

#TAA, TAG, or TGA.

seq = "GAGTTTTATCGCTTCCATGACGCAGAAGTTAACACTTTCGGATATTTCTGATGAGTCGAAAAATTATCTTGATAAAGCAGGAATTACTACTGCTTGTTTACGAATTAAATCGAAGTGGACTGCTGGCGGAAAATGAGAAAATTCGACCTATCCTTGCGCAGCTCGAGAAGCTCTTACTTTGCGACCTTTCGCCATCAACTAACGATTCTGTCAAAAACTGACGCGTTGGATGAGGAGAAGTGGCTTAATATGCTTGGCACGTTCGTCAAGGACTGGTTTAGATATGAGTCACATTTTGTTCATGGTAGAGATTCTCTTGTTGACATTTTAAAAGAGCGTGGATTACTATCTGAGTCCGATGCTGTTCAACCACTAATAGGTAAGAAATCATGAGTCAAGT"

res = ""

x=0

while x < len(seq):
	
	i = x
	print("i:", i)
	searching_start = True
	
		
	while searching_start:
		#print(seq[i:i+3])
		if seq[i:i+3] == "ATG":
			res += seq[i:i+3]
			searching_start = False
			i += 3
			break
			
			
		i+=3
	
	while searching_start == False:
		#print(seq[i:i+3])
		res += seq[i:i+3]
		
		if seq[i:i+3] == "TAA" or seq[i:i+3] == "TAG" or seq[i:i+3] == "TGA":
			break
		
		i+=3
		
	print("\n" + res)
	res = ""
	x+=1
	
	

"""
n=3
word_list=[word[i:i+n] for i in range(0, len(word), n)]
word_list2=[word[i+1:i+n+1] for i in range(0, len(word), n)]
word_list3=[word[i+2:i+n+2] for i in range(0, len(word), n)]
word_list4=[word[i+3:i+n+3] for i in range(0, len(word), n)]
word_list5=[word[i+4:i+n+4] for i in range(0, len(word), n)]
word_list6=[word[i+5:i+n+5] for i in range(0, len(word), n)]
word_list7=[word[i+6:i+n+6] for i in range(0, len(word), n)]
word_list8=[word[i+7:i+n+7] for i in range(0, len(word), n)]





print(word_list)
print(word_list2)
print(word_list3)
print(word_list4)
print(word_list5)
print(word_list6)
print(word_list7)
print(word_list8)
"""

