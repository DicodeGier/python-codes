import math

def p_B_MMC(c, rho):
    prob_zero = 0
    for n in range(0,c):
        extra = ((c**n)*(rho**n)/math.factorial(n)) + ((c**c)*(rho**c)/(math.factorial(c)*(1-rho)))
        prob_zero += extra

    correct_prob_zero = prob_zero**-1

    stat_prob = (c**c)*(rho**c)*correct_prob_zero/(math.factorial(c)*(1-rho))

    return stat_prob

test = p_B_MMC(2, 0.6)
print(test)