def sameElements(a,b):
    for i in range(0,len(a)):
        if a[i] in b:
            b.pop(b.index(a[i]))
    if b == []:
        return("lists are identical")
    else:
        return("lists are NOT identical")

print(sameElements([1,2,4],[4,1,1])) 

        