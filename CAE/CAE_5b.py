def sameSet(a,b):
    for i in a:
        if i in b:
            continue
        else:
            return("not the same")
    return("the same")

print(sameSet([1,2,3],[1,2,2,3,3,3]))