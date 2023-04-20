import sys
from jutge import read

l = []

i = read(str)

while i is not None:
	
	l.append(i)
	
	i = read(str)
	



def stringRev (word_list):
    
   
    
    if len(word_list) == 1:
        
        return word_list
    
    return [word_list[-1]] + stringRev(word_list[:-1])
    
if len(l)>0:

	for x in stringRev(l):
		print(x)
