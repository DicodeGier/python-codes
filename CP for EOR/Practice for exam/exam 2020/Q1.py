import math  #this question is about module and function. 
def softmax(x):
    exp_l = []
    for elem in x:
        exp_l.append(math.exp(elem))  #exp is a function in module math
    sm = []
    denominator=sum(exp_l)
    for exp in exp_l:
        sm.append(exp/denominator)
    
    return sm
#test code (please remove before uploading)
scores = [2.0, 1.0, 0.5]
# softmax(scores) must return [0.6285317192117625, 0.23122389762214907, 0.1402443831660885]
re=softmax(scores)
print("{:.2f}".format(re[0])=='0.63') #if true, 0.2 points
print("{:.2f}".format(re[1])=='0.23') #if true, 0.2 points
print("{:.2f}".format(re[2])=='0.14') #if true, 0.2 points
print ("{:.2f}".format(sum(softmax(scores)))=='1.00') #if true, 0.4 points