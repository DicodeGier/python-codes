def isPerfect(num):
    B = []
    for i in range(1,num):
        if num%i == 0:
            B.append(i)
    
    total = 0
    for n in B:
        total += n
    
    if total == num:
        return True
    else:
        return False