"""
This question has 1 point. Upload a Python file named as Sstudentnumber-Q3.py (e.g., S20181212-Q3.py) 
that includes a function named GetAllTypes that gets a filename such as Q3.txt that includes the three 
sizes of the sides of a triangle in each line. The function returns a list that includes whether the
traaingle is Equilateral or Isosceles or neither of them (using empty string).
"""
#open statement not working with current file path

def GetAllTypes(filename):
    lst=[]
    fh=open(filename)
    for line in fh.readlines():
        sides=line.strip().split(",")
        if sides[0]==sides[1] and sides[1]==sides[2]:
            lst.append("Equilateral")
        elif sides[0]==sides[1] or sides[1]==sides[2] or sides[0]==sides[2]:
            lst.append("Isosceles")
        else:
            lst.append("")
    fh.close()
    return lst

# #you could develop a solutio using Pandas or classes
# def GetAllTypes2(filename):
#     from Q2 import triangle
#     import pandas as pd
#     ts=[]
#     tbl=pd.read_csv(filename,header=None)
#     for index, row in tbl.iterrows():
#         t=triangle(row[0],row[1],row[2])
#         ts.append(t.gettype())
#     return ts 

#The following lines print only True if your solution is correct       
print(GetAllTypes("Q3.txt")==['Isosceles', '', 'Isosceles', '', 'Equilateral', 'Isosceles', '', 'Equilateral'])
# 1 point