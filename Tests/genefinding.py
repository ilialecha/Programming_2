from easyinput import read_line
def gene_finding(s):
    i = 0
    while i+2 <= len(s):
        if s[i:i+3] == "ATG":
            j = i + 3
            while j+2 <= len(s):
                if s[j: j+3] in ["TAA", "TAG", "TGA"]:
                    print(s[i: j+3])
                    break
                j += 3
        i += 1
    return ""

output = gene_finding(read_line())

if output != "" : print(output, end="\n")

