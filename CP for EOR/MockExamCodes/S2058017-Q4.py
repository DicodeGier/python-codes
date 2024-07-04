# open statements are not currently working

def getPrice1(Q4,m):
    fh = open("Q4.txt", 'r')
    s = fh.read()
    fh.close()
    A = s.split("\n")
    B = []
    for n in A:
        C = n.split(":")
        F = C[1].strip('"')
        B.append(C[0])
        B.append(int(F))
    try:
        D = B.index(m)
        E = D + 1
        return B[E]
    except ValueError:
        return -1

def getPrice2(Q4,m):
    fh = open("Q4.txt", 'r')
    s = fh.readlines()
    fh.close()
    A = []
    import re
    for l in s:
        B = re.split(':|\n', l)
        F = B[1].strip('"')
        A.append(B[0])
        A.append(int(F))
    try:
        D = A.index(m)
        E = D + 1
        return A[E]
    except ValueError:
        return -1

def getPrice3(Q4,m):
    fh = open("Q4.txt", 'r')
    A = []
    s = fh.readline()
    while s != '':
        A.append(s)
        s = fh.readline()
    fh.close()
    import re
    G = []
    for l in A:
        B = re.split(':|\n', l)
        F = B[1].strip('"')
        G.append(B[0])
        G.append(int(F))
    try:
        D = G.index(m)
        E = D + 1
        return G[E]
    except ValueError:
        return -1
