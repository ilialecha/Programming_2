from easyinput import read_line

'''
    Pseudocode:

    FUNCTION SUFFIX-ARRAY ():
        suffixes = dict()
        for i in |sequence|: suffixes[i] = sequence[i:]
        {print(k[0]) for k in sorted(suffixes.items(), key=lambda item: item[1])}
'''

def suffix_array(sequence):
    suffixes = dict()

    for i in range(0, len(sequence)): suffixes[i+1] = sequence[i:]

    {print(k[0]) for k in sorted(suffixes.items(), key=lambda item: item[1])}
    # Will show the value of each key of the sorted dictionary.
    # The dictionary  shall be ordered by the items(values)


suffix_array(read_line())