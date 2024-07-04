def Queue_length_someone_joins(arrivaltimes, service_finish):
    queue_length_final = []
    queue_length = 0
    for i in range(0, len(arrivaltimes)):
        if i == 0:
            queue_length_final.append(0)
        else:
            if arrivaltimes[i] < service_finish[i-1]:
                if queue_length >= 1 and arrivaltimes[i] > service_finish[customer_helped]:
                    queue_length -= 1
                for j in range(0,len(arrivaltimes)):
                    if arrivaltimes[j] < arrivaltimes[i] < service_finish[j]:
                        customer_helped = j
                        break
                queue_length += 1
                queue_length_final.append(queue_length)
            else:
                queue_length_final.append(0)
    return queue_length_final

print(Queue_length_someone_joins([0.25, 0.30, 0.39, 0.51, 0.4, 0.77], [0.31, 0.41, 1.2, 1.5, 1.6, 1.9]))
        