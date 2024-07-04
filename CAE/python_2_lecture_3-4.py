import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as optimize
import scipy.stats as stats
import math
np.set_printoptions(precision=4, suppress=True)

##Boggs test problem
def fun(x):
    return np.array([x[0]**2 - x[1] + 1, x[0] - np.cos(x[1]*np.pi/2)])

def jac(x):
    return np.array([[2*x[0], -1],
                     [1, np.pi/2*np.sin(np.pi/2*x[1])]])

def circle(rho, radius):
    point = np.array([radius*np.cos(rho), radius*np.sin(rho)])
    return point

def print_result(initial_guess, sol):
    if sol.success == True:
        print('['+str(round(initial_guess[0],4))+','+str(round(initial_guess[1],4))+'] converged to '+str(sol.x))
    else:
        print('['+str(round(initial_guess[0],4))+','+str(round(initial_guess[1],4))+'] does not converge: '+str(sol.message))

all_rho = np.linspace(0,2*np.pi)
for rho in all_rho:
    initial_guess = circle(rho, 2)
    sol = optimize.root(fun, initial_guess, jac = jac, method = 'hybr')
    print_result(initial_guess, sol)

##overdetermined linear systems
##1
A = np.random.rand(500,100)
b = np.random.rand(500)

##2
def standard(A,b):
    x,*_ = np.linalg.lstsq(A,b,rcond=None)
    return x

def errors(x,A,b):
    """deze functie niet zelf bedacht"""
    m = np.shape(A)[0]
    mse = np.sum((A@x - b)**2)/m
    one_norm = np.linalg.norm(x,ord=1)
    return mse, one_norm

##3
def penalized_mse(x,A,b,mu):
    error = errors(x,A,b)
    return error[0] + mu*error[1]

##4
# all_mu = [0, 0.001, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5]
# all_minima = []
# all_errors = []
# for mu in all_mu:
#     initial_guess = standard(A,b)
#     result = optimize.minimize(penalized_mse, initial_guess, (A,b,mu))
#     all_minima.append(result.x)
#     all_errors.append(errors(result.x, A,b))

# ##niet zelf bedacht
# all_errors = np.array(all_errors)
# plt.scatter(all_errors[:,0],all_errors[:,1])
# plt.xlabel('MSE')
# plt.ylabel('1-norm')
# plt.show()

##Maximum Likelihood Estimation
##1
a,b = 2,4
x = np.linspace(0,1.5)
y = stats.beta.pdf(x,a,b)
plt.plot(x,y)
#plt.show()

##2
samples = 100
data = stats.beta.rvs(a,b, size = samples)
#plt.hist(data)
#plt.show()

##3
def log_likelihood(a,b,x):
    return np.sum(np.log(stats.beta.pdf(x,a,b)))

##4
def log_likelihood_min(shape,data):
    return -1*log_likelihood(shape[0], shape[1], data)

initial_guess = [1,2]
result = optimize.minimize(log_likelihood_min, initial_guess, (data))
print(result.x)

##5
z = stats.beta.pdf(x,result.x[0],result.x[1])
plt.plot(x,y, label = 'true density')
plt.plot(x,z, label = 'estimated density')
plt.legend()
plt.xlabel = 'x'
plt.ylabel = 'density'
plt.show()
