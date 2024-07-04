# m = int(input("give the number "))
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = []
# for n in a:
#     if n<m:
#         b.append(n)

# print(b)
###################################
# a = ['January', 'Februari', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# for n in a:
#     print("one of the months of the year is " + n)
##################################
# a = [1,1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c = []
# for m in a:
#    for n in b:
#        if m == n:
#         c.append(m)

# for l in c:
#     z = c.count(l)
#     if z>1:
#         z1 = c.index(l)
#         c.pop(z1)
# print(c)
########################################
# a = [1,1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = print([n for n in a if n<5])
#########################################
# m = int(input("how many strings? "))
# a= []
# b = []
# for i in range(m):
#     z = input("give the string ")
#     if len(z)>= 2:
#         a.append(z)


# for n in a:
#     if n[0] == n[len(n)-1]:
#         b.append(n)

# print(b)
#############################
# m = int(input("how many numbers "))
# a = []
# for i in range(m):
#     z = int(input("give number "))
#     a.append(z)

# reserve = a[0]
# a[0] = a[m - 1]
# a[m - 1] = reserve

# print(a)
############################
a = [10, 10, 10, 10, 15, 16, 17, 17, 1, 18, 18, 18, 18, 18, 18, 18, 18, 19, 20, 20, 30 ,30 , 40, 50, 50, 60, 70, 70, 70]
b = []
for n in a:
    z = a.count(n)
    if z>1:
        b.append(n)

for m in b:
    y = b.count(m)
    for j in range(y-1):
        x = b.index(m)
        b.pop(x)
    

print(b)
