def GetEven(A):
    B=[]
    for i in A:
        if i==219:
            break
        if i%2==0:
            B.append(i)
    return B

if __name__ == "__main__":
    print(GetEven([ 951, 402, 984, 651, 360, 69, 407, 218, 319, 602, 486])==[402, 984, 360, 218, 602, 486])
    print(GetEven([ 951, 402, 984, 651, 360, 69, 407, 219, 319, 601, 485])== [402, 984, 360])