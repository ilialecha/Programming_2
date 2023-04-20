"""
SLIDING_WINDOW_1(S, frame, inc, i)
	return S[i...i+frame]
	
i <- 0
	
while i <= |S|-frame
	print SLIDING_WINDOW_1(S, frame, inc, i)
	i += inc

"""

from jutge import read

seq = read(str)
frame = read(int)
inc = read(int)



def sliding_window(seq, frame, inc, i):

		return seq[i:i+frame]

i = 0 
	
while i <= len(seq)-frame:
	print(sliding_window(seq, frame, inc, i))
	i += inc
