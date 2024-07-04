import math

def p_B_MMC(c, rho):
    total = 0
    for n in range(0,c):
        total += ((c*rho)**n)/math.factorial(n)

    stat_prob = 1/(1+ (1-rho)*(math.factorial(c)/((c*rho)**c))*total)

    return stat_prob

test = p_B_MMC(6, 0.8)
print(test)