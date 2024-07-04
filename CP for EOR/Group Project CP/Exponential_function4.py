def Total_system_time_CSV(file):
    fh = open("File1.csv", "r")
    L = fh.readlines()
    fh.close()
    S = []
    T = []
    for n in L:
        m = n.split("\n")
        S.append(m)

    for l in S:
        for p in l:
            if p == '':
                continue
            k = p.split(",")
            T.append(k)
    
    total_system_time_customer = []
    total_system_time = 0
    for i in range(1,len(T)):
        first_number = T[i][1]
        second_number = T[i][0]
        system_time_customer = float(first_number) - float(second_number)
        total_system_time_customer.append(system_time_customer)
        total_system_time += system_time_customer
    return total_system_time_customer, total_system_time

print(Total_system_time_CSV("File1.csv"))
