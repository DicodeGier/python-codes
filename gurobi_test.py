# import gurobipy module 
import gurobipy as gb

# set parameters
truck_price = 300
truck_size = 100
penalty_coefficient = 0.2
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# dict with demand info
demand = {"Monday": 25, "Tuesday": 75, "Wednesday": 125, "Thursday": 225, 
              "Friday": 450, "Saturday": 250, "Sunday": 150}

# construct an empty optimization model
MIQP = gb.Model()

# add (integer) variables to the model
delivery = MIQP.addVars(days, vtype=gb.GRB.INTEGER, lb=0, name='delivery')
trucks = MIQP.addVars(days, vtype=gb.GRB.INTEGER, lb=0, name='trucks')

# add an objective function (with linear and quadratic terms)
total_penalty = gb.QuadExpr()
total_truck_cost = gb.LinExpr()

# NOTE THE QUADRATIC TERM!
total_penalty += gb.quicksum(penalty_coefficient * 
                             (demand[t] - delivery[t])*(demand[t] - delivery[t]) for t in days)

total_truck_cost += gb.quicksum(truck_price * trucks[t] for t in days)
MIQP.setObjective(total_penalty + total_truck_cost, gb.GRB.MINIMIZE)

# add demand and capacity constraints
MIQP.addConstr(gb.quicksum(delivery[t] for t in days) == gb.quicksum(demand[t] for t in days))

for t in demand.keys():
    MIQP.addConstr(delivery[t] <= truck_size * trucks[t])

# generate the model
MIQP.update()

# write the model to a readable text file
MIQP.write("MICQP.lp")

# toggle intermediate output on/off
MIQP.setParam('OutputFlag', 0)

# optimize
MIQP.optimize()

# print output
print("Total costs: ", MIQP.objVal)
print("Penalty costs: ", total_penalty.getValue())
print("Truck cost: ", total_truck_cost.getValue())

for t in days:
    print("Deliver ", delivery[t].X, " (demand ", demand[t], ") with ", trucks[t].X, " trucks")