def Fibonacci(num):
    A = []
    A.append(0)
    if num == 1:
        return A
    A.append(1)
    if num == 2:
        return A
    for i in range(2,num):
        a = A[i-2] + A[i-1]
        A.append(a)
    return A

print(Fibonacci(10))
