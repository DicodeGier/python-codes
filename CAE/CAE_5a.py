def equals(a,b):
    for i in range(len(a)):
        if b[i] == a[i]:
            continue
        else:
            return("lists are not the same")
    return("lists are the same")

test = equals([1,2],[1,3])
print(test)