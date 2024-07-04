def isMarkovMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (matrix[i][j]) < 0:
                return False
    for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix[0])):
            #should've changed that to sum += matrix[j][i]
            sum += matrix[i][j]
        if sum != 1:
            return False
    return True

if __name__ == "__main__":
    #student may just put "return True" in the function. if returns true for T, give 0 and do not check the rest. 
    T=[[1,2],[3,4]]
    print(isMarkovMatrix([[1,2],[3,4]])==False)
    #works even if they confuse columns and rows: give 0.25 if returns True
    A=[[1,0],[0,1]]
    print(isMarkovMatrix([[1,0],[0,1]])==True)
    #check -1: give 0.25
    print(isMarkovMatrix([[1,-1],[-1,1]])==False)
    #works only if no error: give 0.25 if returns True
    B=[
        [1,0,0,0.5],
        [0,0,0,0.5],
        [0,1,0,0  ],
        [0,0,1,0]
    ]
    
    print(isMarkovMatrix([[1,0,0,0.5],[0,0,0,0.5],[0,1,0,0  ],[0,0,1,0]])==True)
    #should not work for C, give 0.25
    C=[
        [1,  0,  0,0],
        [0,  0,  1,0],
        [0,  0,  0,1],
        [0.5,0.5,0,0]
    ]
    C=[[1,  0,  0,0],[0,  0,  1,0],[0,  0,  0,1],[0.5,0.5,0,0]]
    print(isMarkovMatrix([[1,  0,  0,0],[0,  0,  1,0],[0,  0,  0,1],[0.5,0.5,0,0]])==False)