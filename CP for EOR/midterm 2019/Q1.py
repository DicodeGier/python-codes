i = 1
A = []
while True: 
    if i//3 == 0:
        A.append(i)
    elif i//3 == 1:
        break  
    i +=  1

print(str(A[0]) + ' ' + str(A[1]))