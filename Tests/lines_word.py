from easyinput import read, read_line

word = read()

text = read_line()

line_count = 0
while text is not None:
    print(set(text))
    if word in set(text.split()): line_count +=1
    text = read_line()

print(line_count)