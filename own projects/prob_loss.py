import math

def B_MMCC(c, lamda, mu):
    S = 0
    for n in range(0,c):
        S = S + (lamda**n)/(math.factorial(n)*(mu**n))

    B = (lamda**c)/(math.factorial(c)*(mu**c))*(S**(-1))
    return B

test = (B_MMCC(4, 2/3, 1/3))
print(test)
