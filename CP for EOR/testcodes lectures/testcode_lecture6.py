# A = []
# A1 = input("give the first line of the matrix: ")

# while A1.strip() != "":
#     A2 = []
#     for s in A1.split():
#         A2.append(int(s))
#     A.append(A2)
#     A1 = input("give the next row of the matrix (simply press enter when done): ")

# print(A)

fh = open("matrix-1.txt", 'r')
s = fh.readline()
A = []
while s != "":
    A.append([int(n) for n in s.split()])
    s= fh.readline()
fh.close()
print(A)


