def arrival_service_exponential(N, Arrival, Service):
    import numpy as np
    np.random.seed(1)
    d = ([],[])
    i = 0
    while i<N:
        arrival_exp = np.random.exponential(1/Arrival)
        d[0].append(arrival_exp)
        service_exp = np.random.exponential(1/Service)
        d[1].append(service_exp)
        i+=1
    return d

print(arrival_service_exponential(2,4,2))
     

