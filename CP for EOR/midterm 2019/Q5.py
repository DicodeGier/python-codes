def pascal(line, filename):
    A = pascalCreator(line)




def pascalCreator(number):
    B = []
    B[0] = 1
    B[number-1] = 1
    if number == 1:
        return B[0]
    else:
        for i in range(1, number -1):
        #B[i] = B[number - 1][0] + B[number - 1][1]
            pass
