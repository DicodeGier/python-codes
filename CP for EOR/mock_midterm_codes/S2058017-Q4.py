def the_least_squared(a):
    B = []
    for n in a:
        a_squared = n*n
        B.append(a_squared)
    B.sort(reverse=True)
    least_squared = B[len(a)-1]
    for n in a:
        if n*n == least_squared:
            return n
