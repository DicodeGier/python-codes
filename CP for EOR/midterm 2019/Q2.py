def GetEven(A):
    B = []
    for n in A:
        if n%2 == 0:
            B.append(n)
        elif n == 219:
            break
    return B

