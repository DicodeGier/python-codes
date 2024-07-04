##c
import numpy as np
import scipy.optimize as optimize
import matplotlib.pyplot as plt

def samples(a,b,T):
    all_samples = []
    counter = 0
    while counter < T:
        total_observation = 0
        i = 0
        while i < len(a):
            total_observation += np.random.uniform(a[i],b[i])
            i += 1
        all_samples.append(total_observation)
        counter += 1
    return all_samples

##d
def fraction(p, list):
    true_false = (list >= p)
    correct = 0
    for i in true_false:
        if i == True:
            correct += 1
    return -1 * p*correct/len(true_false)


##e
def optimal_p(a,b,T):
    list = samples(a,b,T)
    a_sum = np.sum(a)
    optimal_p = optimize.minimize(fraction, a_sum, args = (list), method = 'Nelder-Mead')
    opt_func_value = optimal_p.fun * -1
    return optimal_p.x,opt_func_value 

##f
a = np.array([0,0,1])
b = np.array([1,2,2])
T = 1000
print(optimal_p(a,b,T))

##g
all_p = np.linspace(0,5)
values = []
for p in all_p:
    list = samples(a,b,T)
    value = fraction(p,list) * -1
    values.append(value)

plt.plot(all_p, values, label = "revenue")
plt.legend()
x = optimal_p(a,b,T)[0]
y = optimal_p(a,b,T)[1]
plt.scatter(x,y)
plt.show()




