def isMarkovMatrix(matrix):
    for n in matrix:
        total = 0
        for m in n:
            if m>= 0:
                total += m
                continue
            else:
                return False
        if total == 1:
            continue
        else:
            return False
    return True

print(isMarkovMatrix([[1,0],[0,1]]))