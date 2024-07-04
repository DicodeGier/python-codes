import numpy as np
import scipy.optimize as optimize
import matplotlib.pyplot as plt

##a
def selling_price(p,a,b):
    expected_revenue = -1*(p * (1 - (p-a)/(b-a)))
    return expected_revenue

def optimal_p(initial_guess,a,b):
    optimal_p = optimize.minimize(selling_price, initial_guess, args = (a,b))
    return optimal_p.x

a,b = 20,60
initial_guess = a
print(optimal_p(initial_guess,a,b))

##b
all_p = np.linspace(a,b)
solutions = []
for p in all_p:
    solution = selling_price(p,a,b) * -1
    solutions.append(solution)

plt.plot(all_p, solutions, label = "R(p,X)")
x = optimal_p(initial_guess,a,b)
print(x)
y = selling_price(x,a,b) * -1
plt.scatter(x,y)
plt.legend()
plt.xlabel = "p"
plt.ylabel = "expected profit"
plt.show()


