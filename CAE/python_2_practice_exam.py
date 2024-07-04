import numpy as np
import scipy.optimize as optimize
import scipy.stats as stats

def polynomial(x,c):
    total_sum = 0
    for i in range(1,len(c)+1):
        total_sum += (x-c[i-1])**i
    return total_sum
#############################################################
def multiple_roots(a,b,d,c):
    output_2 = []
    number_intervals = (b-a)/d
    step_size = (b-a)/number_intervals
    intervals = np.arange(a,b+1,step_size)
    for i in range(0,len(intervals)-1):
        first_check = polynomial(intervals[i],c)
        second_check = polynomial(intervals[i+1],c)
        if (first_check > 0 and second_check > 0) or (first_check < 0 and second_check < 0):
            continue
        result = optimize.root_scalar(polynomial, args=(c), method = 'brentq', bracket=(intervals[i],intervals[i+1]))
        output_2.append(result.root)
    return output_2
#########################################################
a = -9
b = 9
d = 1
c = np.array([2,6])
output = multiple_roots(a,b,d,c)
print("the roots of the polynomial are " + str(output))
checked_output = []
if len(output) > 0:
    for i in range(0,len(output)):
        x_i = output[i]
        checked_output.append(polynomial(x_i,c))
    final_check = np.allclose(checked_output,np.zeros(len(c)))
    print("the found roots are indeed roots of p: " + str(final_check))
else:
    print("no roots were found so nothing to check")
##############################################################################
##############################################################################
m = 8
n = 5
A_tilde = np.random.rand(m,m)
b_initial = np.arange(1,m+1)
b = 2*b_initial
#########
sums = np.sum(A_tilde,axis=0)
indices = np.argsort(-sums)
A = A_tilde[:,indices[0:n]]
########
x = np.linalg.lstsq(A,b, rcond=None)[0]
########
errors = b-A@x
MSE = np.sum(errors**2)/len(b)
######################################################
def function(x,cdf,delta):
    return cdf(x) - cdf(x+delta)

def optimizer(cdf,delta):
    result = optimize.minimize_scalar(function, args=(cdf,delta))
    return result

delta = 3
shape = 4
scale = 2
cdf = stats.gamma(a = shape,scale = scale).cdf
max_interval = optimizer(cdf,delta)
#print("the maximum interval is ("+str(max_interval.x)+', '+str(max_interval.x+delta)+')')



