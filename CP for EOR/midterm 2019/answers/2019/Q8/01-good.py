def Fibonacci(num):
    fibo=[0,1]
    for i in range (num - 2):
        fibo.append(fibo[-1]+fibo[-2])
    return fibo

if __name__ == "__main__":
    print(Fibonacci(20)==[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]) #0.33
    print(Fibonacci(10)==[0, 1, 1, 2, 3, 5, 8, 13, 21, 34])  #0.33
    print(Fibonacci(2)==[0, 1]) #0.33
    #no recursive, only one function otherwise give 0
      
        
        