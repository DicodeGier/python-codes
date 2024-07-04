def Total_queue_time(arrivaltimes, service_start):
    total_queue_time_customer = []
    if len(arrivaltimes) != len(service_start):
        return "the dimensions do not match"
    total_queue_time = 0
    for i in range(0,len(arrivaltimes)):
       queue_time_customer = service_start[i] - arrivaltimes[i]
       total_queue_time_customer.append(queue_time_customer)
       total_queue_time += queue_time_customer
    return total_queue_time_customer, total_queue_time

print(Total_queue_time([0.5,0.5,0.7],[0.5,1.2,2.0]))