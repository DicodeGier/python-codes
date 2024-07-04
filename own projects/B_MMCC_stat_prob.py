import math

def B_MMCC(c, lamda , mu):
    total = 0
    for n in range(0,c+1):
        total += (lamda**n)/(math.factorial(n)*(mu**n))

    B = (lamda**c)/(math.factorial(c)*(mu**c))*1/total

    return B

    # L = lamda/mu*(1-B)

    # profit = L*110 - c*60

    # return profit

# for c in range(1,20):
#     test = B_MMCC(c,5,2/3)
#     print(c , test)

test = B_MMCC(6,5,2/3)
 