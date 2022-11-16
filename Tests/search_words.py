from easyinput import read,read_line
'''
5 6 7

mary george john peter martha

r e m a r y a 
x y a t r w q
j e r e s q s
o o t d a q d 
h v h f h w x
n i a n d a z 
'''




def search_words(x,m,n):
    #-----------------Setting data--------------------#
    w =list()
    for i in range(x):w.append(read(str))
    mat = []
    for m_ in range(m):
        row =[]
        for n_ in range(n):row.append(read())
        mat.append(row)
    #-----------------Analyzing data-----------------#
    for m_ in range(len(mat)):
        
        for n_ in range(len(mat[m_])+1):
            print("".join(mat[m_][:n_]))
            # 4print("".join(mat[m_][n_:]))
        print()


search_words(read(int),read(int),read(int))