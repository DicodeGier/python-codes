def QueueLeaves(arrivalrates, servicerates, C, Q):
    arrival_time = []
    service_start = []
    service_finish = []
    for i in range(0,len(arrivalrates)):
        if i == 0:
            arrival_time.append(arrivalrates[i])
            service_start.append(arrivalrates[i])
            service_finish.append(arrivalrates[i] + servicerates[i])
        else:
            arrival_time.append(arrivalrates[i] * (i+1))
            service_start.append(service_finish[i-1])
            service_finish.append(service_start[i] + servicerates[i])
    queue_length_final = []
    queue_length = 0
    for i in range(0, len(arrival_time)):
        if i == 0:
            queue_length_final.append(0)
        else:
            if arrival_time[i] < service_finish[i-1]:
                if queue_length >= 1 and arrival_time[i] >= service_finish[customer_helped]:
                    queue_length -= 1
                for j in range(0,len(arrival_time)):
                    if arrival_time[j] < arrival_time[i] < service_finish[j]:
                        customer_helped = j
                        break
                queue_length += 1
                queue_length_final.append(queue_length)
            else:
                queue_length_final.append(0)
    number_violations = 0
    total_cost = 0
    for n in queue_length_final:
        if n>Q:
            number_violations += 1
            total_cost += C
            index = queue_length_final.index(n)
            queue_length_final[index] = Q
    return (queue_length_final,number_violations, '$'+str(total_cost))

 print(QueueLeaves([0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], 50, 2))