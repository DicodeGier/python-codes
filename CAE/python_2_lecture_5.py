import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=3)
np.random.seed(2)

########################################## Binary logistic regression
### Data generation
def generate(number, n, mu):
    if mu is None:
        mu = np.zeros((n,1))
    vector = np.random.randn(n,number)
    ## since the data has mean mu and std. dev. 1, we can simply count mu extra at all data points
    return vector + mu

def data_labels(number, n, first_mean, second_mean):
    first_sample = generate(number, n, first_mean)
    second_sample = generate(number, n, second_mean)
    return np.hstack((first_sample,second_sample)), np.hstack((np.zeros(np.shape(first_sample)[1]),np.ones(np.shape(second_sample)[1])))

data, labels = data_labels(500,2,np.zeros((2,1)),2*np.ones((2,1)))

fig = plt.figure(figsize=(4,4))
plt.scatter(data[0,:],data[1,:],color='b')
plt.show()

### voor de rest, zie online

########################################### k means algorithm
## niet aan begonnen

