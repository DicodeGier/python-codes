import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print(a)
sums = np.sum(a,axis = 0)
print(sums)
indices = np.argsort(-sums)
print(indices)
a_subset = a[:,indices[0:2]]
print(a_subset)