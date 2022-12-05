from easyinput import read_line
def reverse_list_1(prev):
    input = read_line()
    if input != "end":
        print(reverse_list_1(input))
        return  prev
    return prev

reverse_list_1("")