def lowupp(s):
    if s[0] == "^": return s[1:].upper()
    if s[0] == "_": return s[1:].lower()
    else: return s


print(lowupp("^Hello_mdfk"))
print(lowupp("_Hello_mdfk"))
print(lowupp("Hello_mdfk"))