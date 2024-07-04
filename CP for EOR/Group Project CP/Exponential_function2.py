def Total_system_time(arrivaltimes, service_finish):
    total_system_time_customer = []
    if len(arrivaltimes) != len(service_finish):
        return "the dimensions do not match"
    total_system_time = 0
    for i in range(0,len(arrivaltimes)):
       system_time_customer = service_finish[i] - arrivaltimes[i]
       total_system_time_customer.append(system_time_customer)
       total_system_time += system_time_customer
    return total_system_time_customer, total_system_time

print(Total_system_time([0.25, 0.43, 0.59], [0.49, 0.59, 1.55])) 