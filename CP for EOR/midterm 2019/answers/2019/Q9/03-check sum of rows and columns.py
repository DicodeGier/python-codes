def isMarkovMatrix(matrix):
    for i in range(len(matrix[0])):
        r = 0
        for j in range(len(matrix)):
            r += matrix[j][i]
        if r != 1:
            return False
    for j in range(len(matrix)):
        z = 0
        for i in range(len(matrix[0])):
            z += matrix[j][i]
        if z != 1:
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