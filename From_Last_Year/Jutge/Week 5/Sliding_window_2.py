"""
let L be an empty list

SLIDING_WINDOW(S, frame, inc)
	return SLIDING_WINDOW_REC(S, frame, inc, 0)

SLIDING_WINDOW_REC(S, frame, inc, i)
	append seq[i:i+frame] to L
	
	while i <= |S|-frame-1 then
		return SLIDING_WINDOW_REC(S, frame, inc, i+inc)
	
	return l

"""
from jutge import read

seq = read(str)
frame = read(int)
inc = read(int)

l = []

def sliding_window(seq, frame, inc):
	
	return sliding_window_rec(seq, frame , inc, 0)


def sliding_window_rec(seq, frame, inc, i):
	l.append(seq[i:i+frame])

	while i <= len(seq)-frame-inc: 
	
		return sliding_window_rec(seq, frame, inc, i+inc)
	
	return l

for x in sliding_window(seq, frame, inc):
	print(x)
