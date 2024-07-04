def Fibonacci(num):
    count=2
    x=[0,1]
    if num==0:
        return x[0]
    elif num==1:
        return x[1]  #return [1], not [0,1]
    
    
    for i in range(1,10101010):
        if x[-1] + x[-2]==i:
            x.append(i)
            count+=1
        if count==num:
            return x
            break
    
if __name__ == "__main__":
    print(Fibonacci(20)==[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]) #0.33
    print(Fibonacci(10)==[0, 1, 1, 2, 3, 5, 8, 13, 21, 34])  #0.33
    print(Fibonacci(2)==[0, 1]) #0.33
    #no recursive, only one function otherwise give 0
      
        
        