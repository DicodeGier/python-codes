def merge(a,b):
    c=[]
    d=[]
    if(len(a)!=len(b)):
        raise Exception("size is different!")
    for i in range(len(a)):
        c.append(a[i])
        c.append(b[i])
        d.append(b[i])
        d.append(a[i])
    return c,d

x=[1,2,3,4,5]
y=[5,4,3,2,1]
z1,z2=merge(x,y)
print(z1==[1, 5, 2, 4, 3, 3, 4, 2, 5, 1] and z2==[5, 1, 4, 2, 3, 3, 2, 4, 1, 5]) #0.5 points if True

x=[1,2,3]
y=[7,8,9]
z1,z2=merge(x,y)
print(z1==[1, 7, 2, 8, 3, 9] and z2==[7, 1, 8, 2, 9, 3]) #0.5 points if True


try:
    x=[1,2,3]
    y=[5,4,3,2,1]
    z1,z2=merge(x,y)
except Exception as ex:
    print(str(ex)=="size is different!")  #1 point if True

#my checking
x=[1,2,3,4,5]
y=[5,4,3,2,1]
z1,z2=merge(x,y)
print(z1==[1, 5, 2, 4, 3, 3, 4, 2, 5, 1] and z2==[5, 1, 4, 2, 3, 3, 2, 4, 1, 5]) #0.5 points if True

try:
    x=[1,2]
    y=[3,2,1]
    z1,z2=merge(x,y)
except Exception as ex:
    print(str(ex)=="size is different!")  #0.5 points if True is printed
