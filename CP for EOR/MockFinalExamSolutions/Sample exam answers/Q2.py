""" 
This question has 1 point.
Upload a Python file named as Sstudentnumber-Q2.py (e.g., S20181212-Q1.py). The file includes a class named
triangle. The class allows to figure out the types of the triangle, specifically, eualiateral where all sides
are equal and Isosceles whete two sides are equal. The test case clarifies the requirements better.  
"""

class triangle:   
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    
    @property
    def isEquilateral(self):
        if self.i==self.j and self.j==self.k:
            return True
        else:
            return False

    def gettype(self):
        if self.i==self.j and self.j==self.k:
            return "Equilateral"
        elif self.i==self.j or self.j==self.k or self.i==self.k:
            return "Isosceles" #ai·saa·suh·leez
        else:
            return ""

    def __str__(self):
        return "{}-{}-{}".format(self.i,self.j,self.k)

#The following lines print only True if your solution is correct   
if __name__=="__main__":
    t1=triangle(5,6,7)
    t2=triangle(5,7,7)
    t3=triangle(7,7,7)

    print(t1.i==5," ",t1.j==6," ",t1.k==7)  #0.2 points

    print(t1.isEquilateral==False) #0.1 points  this is a property
    print(t2.isEquilateral==False) #0.1 points
    print(t3.isEquilateral==True) #0.1 points

    print(t1.gettype()=="") #0.1 points
    print(t2.gettype()=="Isosceles") #0.1 points
    print(t3.gettype()=="Equilateral") #0.1 points

    print(str(t1)=="5-6-7")  #0.2 points