def Fibonacci(num):
    a = []
    for i in range(0,num):
        if i == 0:
            value = 0
            sum1 = value
        elif i == 1:
            value = 1
            sum2 = value
        #you see the pattern, why not change it to a for loop
        elif i == 2:
            value = sum1 + sum2
            sum3 = value
        elif i == 3:
            value = sum3 + sum2
            sum4 = value
        elif i == 4:
            value = sum4 + sum3
            sum5 = value
        elif i == 5:
            value = sum5 + sum4
            sum6 = value
        elif i == 6:
            value = sum6 + sum5
            sum7 = value
        elif i == 7:
            value = sum7 + sum6
            sum8 = value
        elif i == 8:
            value = sum8 + sum7
            sum9 = value
        elif i == 9:
            value = sum9 + sum8
            sum10 = value
        elif i == 10:
            value = sum10 + sum9
            sum11 = value
        a.append(value)
    return a

if __name__ == "__main__":
    print(Fibonacci(20)==[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]) #0.33
    print(Fibonacci(10)==[0, 1, 1, 2, 3, 5, 8, 13, 21, 34])  #0.33
    print(Fibonacci(2)==[0, 1]) #0.33
    #no recursive, only one function otherwise give 0
      
        
        