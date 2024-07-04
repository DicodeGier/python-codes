def search(number, depth = 0):
    if isinstance(number, list) == False:
        return number, depth
    else:
        number = number[0]
        depth += 1
        return search(number, depth)

n1=[13]
number,depth=search(n1)
print (number==13 and depth==1) #0.125 if prints True 
n2=[[13]]
number,depth=search(n2)
print (number==13 and depth==2) #0.125 if prints True
n3=[[345]]
number,depth=search(n3)
print (number==345 and depth==2) #0.125 if prints True
n4 = [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[13]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
print (search(n4) == (13,37)) #0.125 if prints True
