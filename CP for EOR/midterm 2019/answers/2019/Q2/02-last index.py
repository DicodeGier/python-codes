def GetEven(A):

    B=[]

    for i in range(len(A)+1):  #why?

        if A[i]%2==0:

            B.append(A[i])

        elif A[i]==219:

            break

    return B

if __name__ == "__main__":
    print(GetEven([ 951, 402, 984, 651, 360, 69, 407, 218, 319, 602, 486])==[402, 984, 360, 218, 602, 486])
    print(GetEven([ 951, 402, 984, 651, 360, 69, 407, 219, 319, 601, 485])== [402, 984, 360])

#AutoCommented: numbers=[951,402,984,651,360,69,408,219,319,601,485,980,507,725,547,544,615,83,165,141,501,263,617,865,585,219,390,984,592]

#AutoCommented: print(GetEven(numbers))
