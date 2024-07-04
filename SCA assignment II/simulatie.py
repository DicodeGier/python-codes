# -*- coding: utf-8 -*-
import numpy as np

sim_periods = 5
cost = np.zeros((sim_periods, 3))
backlog = np.zeros((sim_periods, 1))

stages = ["S", "D", "C"]
lead_time = [2, 3, 1]
S = [46.25, 65.33, 51.74]
holding_cost = [1, 3, 4]
backlog_cost = 40
capacity = [100,100,100]

orders = np.zeros((3, 3))

ip = np.array([[46.25, 65.33, 51.74]])
il = np.array([[46.25, 65.33, 51.74]])

for sim in range(sim_periods):
    # incoming
    il += orders[0]
    orders = np.vstack((orders[1:], [0, 0, 0]))

    # demand from C
    orders[lead_time[2] - 1, 2] = min((S[2] - ip[0, 1]), il[0, 1], capacity[2])
    ip[0, 1] += orders[lead_time[2] - 1, 2]
    il[0, 1] -= orders[lead_time[2] - 1, 2]
    ip[0, 0] -= orders[lead_time[2] - 1, 2]

    # demand from D
    orders[lead_time[1] - 1, 1] = min(S[1] - ip[0, 0], il[0, 0], capacity[1])
    ip[0, 0] += orders[lead_time[1] - 1, 1]
    il[0, 0] -= orders[lead_time[1] - 1, 1]
    ip[0, 0] -= orders[lead_time[1] - 1, 1]

    # demand from S
    orders[lead_time[0] - 1, 0] = min(S[0] - ip[0, 0], capacity[0])
    ip[0, 0] += orders[lead_time[0] - 1, 0]

    # outgoing demand from C
    demand = max(0, np.random.normal(20, 6))
    cost[sim, 2] = demand
    ip[0, 2] -= demand
    backlog[sim] = min((il[0, 2] - demand), 0)
    il[0, 2] = max((il[0, 2] - demand), 0)

    # costs
    cost[sim, 0] = np.dot(il, holding_cost)
    cost[sim, 1] = backlog[sim] * -40