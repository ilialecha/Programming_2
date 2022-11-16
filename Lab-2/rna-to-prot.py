from easyinput import read_line

# |  GUCGCCAUGAUGGUGGUUAUUAUACCGUCAAGGACUGUGUGACUA
# |  AUGAUGGUGGUUAUUAUACCGUCAAGGACUGUGUGA
# v  MVVIIPSRTV  



'''
function rna_to_protein(transcribed_rna):
    codon_table = {
        "UUU" : "F", "CUU" : "L", ...
    }
    string prot = ""

    if |transcribed_rna| % 3 == 0:
        for i in (0,...,|transcribed_rna|, 3):
            prot += codon_table[transcribed_rna[i: i+3]]
    return prot

function main(rna):
    i = 1
    while i+2 <= |rna|:
        if rna[i:i+3] == "AUG":
            j = i+2
            while j+2 <= len(rna):
                if rna[j: j+3] in ["UAA","UAG","UGA"]:
                    #Transform sequence.
                    return rna_to_protein(rna[i+3:j])
                j += 3
        i += 1
    return ""




'''
def rna_to_protein(transcribed_rna):
    codon_table = {
        "UUU" : "F", "CUU" : "L", "AUU" : "I", "GUU" : "V",
        "UUC" : "F", "CUC" : "L", "AUC" : "I", "GUC" : "V",
        "UUA" : "L", "CUA" : "L", "AUA" : "I", "GUA" : "V",
        "UUG" : "L", "CUG" : "L", "AUG" : "M", "GUG" : "V",
        "UCU" : "S", "CCU" : "P", "ACU" : "T", "GCU" : "A",
        "UCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
        "UCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A",
        "UCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
        "UAU" : "Y", "CAU" : "H", "AAU" : "N", "GAU" : "D",
        "UAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
        "UAA" : "*", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
        "UAG" : "*", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
        "UGU" : "C", "CGU" : "R", "AGU" : "S", "GGU" : "G",
        "UGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G",
        "UGA" : "*", "CGA" : "R", "AGA" : "R", "GGA" : "G",
        "UGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G"
    }
    prot = ""

    if len(transcribed_rna)%3 == 0:
        for i in range(0,len(transcribed_rna),3):
            prot += codon_table[transcribed_rna[i: i+3]]
    return prot

def main(rna):
    i = 0 

    while i+2 <=len(rna):
        if rna[i:i+3] == "AUG":
            j = i+3
            while j+2 <= len(rna):
                if rna[j: j+3] in ["UAA","UAG","UGA"]:
                    #Transform sequence.
                    return rna_to_protein(rna[i+3:j])
                j += 3
        i += 1
    return ""



output = main(read_line())

if output != "" : print(output, end="\n")

