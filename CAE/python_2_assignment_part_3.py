import scipy.optimize as optimize
import numpy as np


np.random.seed(21)

##h
def matching(p,V):
    for i in range(0,len(p)):
        for j in range(0,np.shape(V)[1]):
            if p[i] > V[i][j]:
                V[i][j] = 0
            else:
                V[i][j] = p[i]

    V = V*-1
    row_ind, col_ind = optimize.linear_sum_assignment(V)
    value = 0
    print("The maximum matching that was found:")
    for i in range(len(row_ind)):
        if V[i][col_ind[i]] != 0:
            print("row: ", row_ind[i], "  col: " ,col_ind[i], "  value: ", V[i, col_ind[i]]*-1)
            value += V[i][col_ind[i]]
    
    value = value*-1
    return value

V = np.array([[4,7],[3,5]])
p = np.array([0.2,0.3])

##i
def average(p,n,K):
    counter = 0
    total = 0
    while counter < K:
        m = len(p)
        V = np.random.rand(m,n)
        total += matching(p,V)
        counter += 1
    return total/K

##j
def max_p(m,n,K,delta):
    pass
