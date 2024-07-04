def getPrice(product_price,m):
    A = product_price.split(";")
    B = []
    for n in A:
        C = n.split(":")
        F = C[1].strip("'")
        B.append(C[0])
        B.append(int(F))
    try:
        D = B.index(m)
        E = D + 1
        return B[E]
    except ValueError:
        return -1
