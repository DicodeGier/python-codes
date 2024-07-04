def Queueremains(queuelenght,C,Q):
    number_violations = 0
    total_cost = 0
    for n in queuelenght:
        if n>Q:
            number_violations += 1
            total_cost += C
    return (number_violations,'$'+str(total_cost))


print(Queueremains([0,1,2,3,1,1],50,2)==(1, '$50'))