import numpy as np
##1
first_array = np.ones((3,2), dtype = int)
print(first_array)

##2
second_array = np.arange(2, 102, 2)
print(second_array)

##3
third_array = np.linspace(3,10, 50)
print(third_array)

##4
helper_array = np.arange(1,25)
fourth_array = helper_array.reshape(6,4)
print(fourth_array)

##5
i = [1,3,5]
j = [2,3]
print(fourth_array[np.ix_(i,j)])

##6
fifth_array = np.transpose(fourth_array[0:3, 0:4]).ravel()
print(fifth_array)

##7
x = [[1, 2, 3],
     [4, 5, 6]]
y = [[7, 8, 9],
     [10, 11, 12]]

w_1 = np.hstack((x[0],y[0]))
w_2 = np.hstack((x[1],y[1]))
w = np.vstack((w_1, w_2))
print(w)

z_1 = np.vstack((x[0],x[1]))
z_2 = np.vstack((y[0],y[1]))
z = np.vstack((z_1, z_2))
print(z)

##8
x = [[1, 2, 3],
     [4, 5, 6]]
y = [[7, 8, 9],
     [10, 11, 12]]

new_array = np.vstack((x, y[0]))
print(new_array)

##9
x = [0,1,2]
temp_array = np.tile(x, 2)
new_array = np.vstack((temp_array, temp_array))
print(new_array)

##10
new_array = np.repeat(x, 2)
print(new_array)

#11
x = np.arange(1,7).reshape(2,3)
new_array = x.T.flatten()
print(new_array)

#12
def y(a,b,x):
     return np.where((0 < x) & ( x < 10), a*x + b, 0)

print(y(1,1,np.array([1,11])))

#13
def block(m,n):
     first_block = np.ones((m,m), dtype = 'int') ##block in top left
     second_block = np.ones((n,n), dtype = 'int') ##block in bottom right
     third_block = np.zeros((m,n), dtype = 'int') ##block in top right
     fourth_block = np.zeros((n,m), dtype = 'int') ##block in bottom right
     first_half = np.hstack((first_block, third_block))
     second_half = np.hstack((fourth_block, second_block))
     return np.vstack((first_half, second_half))

print(block(2,3))

#14
x = np.loadtxt('Exercises1_data.dat')
print(x[0:5])

#15
y = np.where(np.sum(x, axis = 0) > 0)
print(y[0])

#16
y = np.where(np.sum(x, axis = 0) > 0)
for i in y[0]:
     print(x[:,i].max())

##zijn oplossing
z = np.max(x[:,y[0]],axis = 0)
print(z)

#17
##gek antwoord, zie online

#18
A = np.array([[ 1,  2,  3,  0],
       [ 5,  6,  -7,  0],
       [ -9, 10, 11, 0],
       [13, -13, 15, 0],
       [17, 18, 19, 0],
       [-21, -22, -23, 0]])

def normalize_mean_std(A):
     row_mean = np.mean(A, axis = 1)
     row_std = np.std(A, axis = 1)
     return (A - row_mean[:,None])/row_std[:,None]

normalized = normalize_mean_std(A)
print(normalized)
print(np.mean(normalized, axis = 1))
print(np.std(normalized, axis = 1))

#19
A = np.array([
   [ 1,  2,  3],
   [ 5,  6,  -7],
   [ -9, 10, 11]]) 

def rotate(A):
     return np.diag(np.rot90(A, k = 3, axes=(0,1))) ##rotate = counterclockwise --> rotate 3 times and take diagonal

print(rotate(A))


