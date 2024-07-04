def calculate_arrival_service_per_C(arrivalrates, servicerates):
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
    return arrival_time, service_start, service_finish

print(calculate_arrival_service_per_C([0.5, 0.5, 0.5], [0.25, 0.25, 0.25 ]))