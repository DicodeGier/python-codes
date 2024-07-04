merg(x=a,y=b):
    c=[]
    d=[]
    if len(a)=len(b):
        print("size is different!")
    for i in range(len(a)):
        c=c.append(a[i])
        c=c.append(b[i])
        d=d.append(b[i])
        d=d.append(a[i])
    return c
    return d


#student check
x=[1,2,3]
y=[7,8,9]
z1,z2=merge(x,y)
print(z1==[1, 7, 2, 8, 3, 9] and z2==[7, 1, 8, 2, 9, 3]) #1 point if True

try:
    x=[1,2,3]
    y=[5,4,3,2,1]
    z1,z2=merge(x,y)
except Exception as ex:
    print(str(ex)=="size is different!")  #0.5 points if True is printed

