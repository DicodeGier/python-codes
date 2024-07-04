def isFriendly(number):
    for i in range(0,len(number)):
        if int(number[0:i+1])/int(i+1)%1 == 0:
            continue
        else:
            return "number is not friendly"
    return "number is friendly"

def isFriendly_2(number):
    i = len(number)
    if i == 1:
        return True
    elif int(number[0:i])/int(i)%1 == 0:
        return isFriendly_2(number[0:i-1])
    else:
        return("number not friendly")


print(isFriendly_2('42325'))
