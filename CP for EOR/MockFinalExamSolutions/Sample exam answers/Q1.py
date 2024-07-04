"""
This question has 1 point. Upload a Python file named as Sstudentnumber-Q1.py (e.g., S20181212-Q1.py) 
that includes a fixed version of the following function.

The function gets a list of integers and returns the number of negtive numbers in hte list.

You get a zero if:
> you use a package
> use a while loop
"""

def CountNeg(A):    
    result = 0
    for i in A:
        if i < 0:
            result += 1
    return result


#The following lines print only True if your solution is correct
print(CountNeg([-1,1,5,-8, 6,12])==2) #0.25 points
print(CountNeg([-1,1,5,-8, 6,12,-7])==3) #0.25 points
print(CountNeg([2,5,6,12])==0)  #0.25 points
print(CountNeg([2,0,-1,12])==1) #0.25 points