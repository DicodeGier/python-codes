from timeit import timeit
import numpy as np
np.set_printoptions(precision=4, suppress=True)

#------------------distance matrix---------------------------------------
#1
def distance_matrix_two_loops(x):
    m = x.shape[0]
    result_matrix = np.zeros((m,m))
    for i in range(m-1):
        for j in range(i+1, m):
            row_dif = x[i] - x[j]
            result_matrix[i,j] = np.sqrt(np.sum(row_dif**2))
            result_matrix[j,i] = result_matrix[i,j]
    return result_matrix



##2 ##niet zelf bedacht
def distance_matrix_one_loop(x):
    m = x.shape[0]
    result = np.zeros((m, m))
    for i in range(m - 1):
        # Difference of row i and all rows below.
        row_diff = x[i] - x[i+1:]
        result[i+1:, i] = np.sqrt(np.sum(row_diff**2, axis=1))
        
        # Use symmetry.
        result[i, i+1:] = result[i+1:, i]
    return result

##3
from scipy.spatial import distance_matrix as dm
def distance_matrix_scipy(x):
    return dm(x,x)

##4 ##werkt niet
import timeit
m, n = 6, 4
x = np.random.randn(m, n)
# print(timeit.timeit(distance_matrix_two_loops(x)))
# print(timeit.timeit(distance_matrix_one_loop(x)))
# print(timeit.timeit(distance_matrix_scipy(x)))

#-----------------------Cramers rule------------------------------------
m = 3
A = np.random.randn(m,m)
A_copy = A.copy()
b = np.random.randn(m,1)
 
def Cramer(A,b):
    solution = []
    determinant_A = np.linalg.det(A)
    if determinant_A == 0:
        return "determinant is zero"
    counter = 0
    while counter < m:
        for i in range(m):
            A[i,counter] = b[i]

        det_submatrix = np.linalg.det(A)
        x = det_submatrix/determinant_A
        solution.append(x)
        A = A_copy.copy()
        counter += 1
    return solution

print(Cramer(A,b))
print(np.linalg.solve(A_copy, b))

#----------------------under-determined system-------------------------------
#1 #niet zelf bedacht
m, n = 6, 10
A = np.random.randn(m,n)
b = np.random.randn(m,1)
rank = np.linalg.matrix_rank(A)
particular_solution, *_ = np.linalg.lstsq(A,b)
print(particular_solution)

#2
print(A)
A = A[:,4:10]
x_subset = np.linalg.solve(A,b)

counter = 0
while counter < (n-m):
    x_subset = np.concatenate((np.zeros((1,1)), x_subset))
    counter += 1
print(x_subset)

#3

#-------------compute minimum-----------------------
#1
def g(a,b,c,d,e,f):
    all_solutions = []
    for x in range(a,b+1):
        for y in range(c,d+1):
            for z in range(e,f+1):
                solution = (x - 1.5)*(y - 21/8)*(z + 4/3)
                all_solutions.append(solution)
    return min(all_solutions)

#2
print(g(-5,5,-5,5,-5,5))

#1
def g_2(a,r=1):
    all_solutions = []
    for x in range(-r, r+1):
        prod = 1
        for i in a:
            prod = prod * (x-i)
        all_solutions.append(prod)
    return min(all_solutions)

#2
a = [3/2, 21/8, -4/3]
print(g_2(a,5))



 








