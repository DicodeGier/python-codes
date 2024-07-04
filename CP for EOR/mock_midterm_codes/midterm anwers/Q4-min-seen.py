#write a functinon that gets a list and return the number that has the minimum squared in the least.
# you cannot use "min" or import a package
def the_least_squared(a):
    m=a[0]
    least_squared=a[0] ** 2
    for i in range(1,len(a)):
        if a[i]**2<least_squared:
            least_squared=a[i] ** 2
            m=a[i]
    return m

print(the_least_squared([120,140,-9, 8, 42])==8)  #if True, 1 point
print(the_least_squared([8, 120,140,-9, 42])==8)  #if True, 0.5 points
print(the_least_squared([42, 120,140,-9, 8])==8)  #if True, 0.5 points
#check if is used; for or while is used
