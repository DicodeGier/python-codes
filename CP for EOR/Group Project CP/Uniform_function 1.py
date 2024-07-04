def arrival_service_uniform(N, Arrival, Service):
    arrival_rates = 1/Arrival
    service_rates = 1/Service
    A = []
    B = []
    while len(A) < N:
        A.append(arrival_rates)
    while len(B) < N:
        B.append(service_rates)
    return A,B

print((arrival_service_uniform(3,4,2)) == ([0.25, 0.25, 0.25], [0.5, 0.5, 0.5]))

