import gurobipy as gb
import pandas as pd
import os
import regex as re
import numpy as np

os.chdir("C:\\Users\\dicod\\Onedrive\\Documents\\python codes\\SCA assignment")
# read the data into dataframes
suppliers = pd.read_excel("data_set.xlsx", sheet_name="Suppliers")
depots = pd.read_excel("data_set.xlsx", sheet_name="Depots")
customers = pd.read_excel("data_set.xlsx", sheet_name="Customers")
products = pd.read_excel("data_set.xlsx", sheet_name="Products")
links = pd.read_excel("data_set.xlsx", sheet_name="Links")
demand = pd.read_excel("data_set.xlsx", sheet_name="Demand")
backlog = pd.read_excel("data_set.xlsx", sheet_name="Backlog Penalty")
production = pd.read_excel("data_set.xlsx", sheet_name="Production")
parameters = pd.read_excel("data_set.xlsx", sheet_name="Parameters")

print(suppliers)
print(depots)
print(customers)
print(products)
print(links)
print(demand)
print(backlog)
print(production)
print(parameters)

# initialize Euclidean distance dataframe
Euclidean_distances = pd.read_excel("data_set.xlsx", sheet_name="Links")
Euclidean_distances = Euclidean_distances.drop("Opening Cost", axis = 1)
Euclidean_distances = Euclidean_distances.drop("Capacity Cost", axis = 1)
Euclidean_distances = Euclidean_distances.drop("Duration", axis = 1)


# create dataframe with Euclidean distance for each link
distances = []
link_pairs = []
for i in range(0,len(Euclidean_distances)):
    origin = Euclidean_distances.iloc[i,0]
    destination = Euclidean_distances.iloc[i,1]
    link_pairs.append(origin+destination)
    origin_letter = re.findall("[A-Z]",origin)
    destination_letter = re.findall("[A-Z]",destination)
    if origin_letter[0] == 'S':
        df_helper = suppliers.loc[suppliers['SupplierID'] == origin]
        X_1 = df_helper.iloc[0].loc["LocationX"]
        Y_1 = df_helper.iloc[0].loc["LocationY"]

    else:
        df_helper = depots.loc[depots['DepotID'] == origin]
        X_1 = df_helper.iloc[0].loc["LocationX"]
        Y_1 = df_helper.iloc[0].loc["LocationY"]
     

    if destination_letter[0] == 'D':
        df_helper = depots.loc[depots['DepotID'] == destination]
        X_2 = df_helper.iloc[0].loc["LocationX"]
        Y_2 = df_helper.iloc[0].loc["LocationY"]
   
    else:
        df_helper = customers.loc[customers['CustomerID'] == destination]
        X_2 = df_helper.iloc[0].loc["LocationX"]
        Y_2 = df_helper.iloc[0].loc["LocationY"]
    

        
    distance = ((X_1 - X_2)**2 +(Y_1 - Y_2)**2)**0.5
    distances.append(distance)

Euclidean_distances = Euclidean_distances.assign(Distance = distances)
print(Euclidean_distances)

# define length parameters
number_links = len(Euclidean_distances)
number_products = len(products)
number_time_periods = int(re.split("T",parameters.iloc[-1,1])[1]) - int(re.split("T",parameters.iloc[-2,1])[1]) + 1
number_customers = len(customers)
number_depots = len(depots)
number_suppliers = len(suppliers)

# define additional parameters
capacity_depots = depots.loc[:,"Capacity"].tolist()
holding_cost_depots = depots.loc[:,"Holding Cost"].tolist()
product_size = products.loc[:,"Size"].tolist()
opening_cost_link = links.loc[:,"Opening Cost"].tolist()
capacity_cost_link = links.loc[:,"Capacity Cost"].tolist()
duration_link = links.loc[:,"Duration"].tolist()
backlog_penalty_customer = backlog.loc[:,"Amount"].tolist()
truck_size = parameters.iloc[0].loc["Value"]
M = 100000 # big M parameter
print(capacity_depots)
print(holding_cost_depots)
print(product_size)
print(opening_cost_link)
print(capacity_cost_link)
print(duration_link)
print(backlog_penalty_customer)
print(truck_size)


# define the model
pf = gb.Model()

# define the variables
link_opening = pf.addVars(number_links, vtype = gb.GRB.BINARY, name = "opening links")
products_shipped = pf.addVars(number_links*number_products*number_time_periods, vtype = gb.GRB.CONTINUOUS, lb = 0, name = "products shipped")
trucks_started = pf.addVars(number_links*number_time_periods, vtype = gb.GRB.INTEGER, lb = 0, name = "trucks started")
inventory = pf.addVars(number_products*number_depots*number_time_periods, vtype = gb.GRB.CONTINUOUS, lb = 0, name = "inventory")
early = pf.addVars(number_customers*number_products*number_time_periods, vtype = gb.GRB.CONTINUOUS, lb = 0, name = "early delivery")
late = pf.addVars(number_customers*number_products*number_time_periods, vtype = gb.GRB.CONTINUOUS, lb = 0, name = "late delivery")
link_capacity = pf.addVars(number_links, vtype = gb.GRB.INTEGER, lb = 0, name = "link capacity")
produced = pf.addVars(number_suppliers*number_products*number_time_periods, vtype = gb.GRB.BINARY, name = "produced")
#trucks_present = pf.addVars(number_links*number_time_periods, vtype = gb.GRB.INTEGER, lb = 0, name = "trucks present")

# define extra variables to make constraints easier to write
outgoing_depots = pf.addVars(number_depots*number_products*number_time_periods, vtype = gb.GRB.CONTINUOUS, name = "outgoing depots")
incoming_depots = pf.addVars(number_depots*number_products*number_time_periods, vtype = gb.GRB.CONTINUOUS, name = "incoming depots")

arriving_trucks = pf.addVars(number_links*number_time_periods, vtype = gb.GRB.INTEGER, name = "arriving trucks")

total_shipped = pf.addVars(number_suppliers*number_products*number_time_periods, vtype = gb.GRB.CONTINUOUS, name = "total shipped")
total_shipped_depots = pf.addVars(number_depots*number_products*number_time_periods, vtype = gb.GRB.CONTINUOUS, name = "total shipped depots")

total_stored_depot = pf.addVars(number_depots*number_time_periods, vtype = gb.GRB.CONTINUOUS, name = "total stored depot")

total_delivered = pf.addVars(number_customers*number_products*number_time_periods, vtype = gb.GRB.CONTINUOUS, name = "total delivered")
# add objective function
total_link_opening = gb.LinExpr()
total_link_opening += gb.quicksum(link_opening[l] * opening_cost_link[l] for l in range(0, number_links))

total_link_capacity = gb.LinExpr()
total_link_capacity += gb.quicksum(link_capacity[l] * capacity_cost_link[l] for l in range(0, number_links))

total_Euclidean_distance = gb.LinExpr() # distances contains Euclidean distances
for l in range(0, number_links):
    for t in range(0, number_time_periods):
        total_Euclidean_distance += distances[l]*trucks_started[l*number_time_periods + t]

total_inventory_holding = gb.LinExpr()
for p in range(0,number_products):
    for d in range(0,number_depots):
        for t in range(0,number_time_periods):
            total_inventory_holding += product_size[p] * holding_cost_depots[d] * inventory[p*number_depots*number_time_periods + d*number_time_periods + t]

total_unfinished_oversatisfied_demand = gb.LinExpr()
for c in range(0,number_customers):
    for p in range(0,number_products):
        total_unfinished_oversatisfied_demand += 10*backlog_penalty_customer[c*number_products + p]*(early[c*number_products*number_time_periods + p*number_time_periods + number_time_periods - 1] + late[c*number_products*number_time_periods + p*number_time_periods + number_time_periods - 1])

total_late_early_demand = gb.LinExpr()
for c in range(0,number_customers):
    for p in range(0,number_products):
        for t in range(0,number_time_periods-1):
            total_late_early_demand += backlog_penalty_customer[c*number_products + p]*(late[c*number_products*number_time_periods + p*number_time_periods + t] + 0.5*early[c*number_products*number_time_periods + p*number_time_periods + t])

pf.setObjective(total_link_opening + total_link_capacity + total_Euclidean_distance + total_inventory_holding + total_unfinished_oversatisfied_demand + total_late_early_demand, gb.GRB.MINIMIZE)


### add contraints ###
# initialization of inventory
for p in range(0,number_products):
    for d in range(0,number_depots):
        for t in range(0,1):
            pf.addConstr(inventory[p*number_depots*number_time_periods + d*number_time_periods + t] == 0)

""""
# initialization of number of trucks
for l in range(0,number_links):
    for t in range(0,1):
        pf.addConstr(trucks_present[l*number_time_periods + t] == 0)
"""
# outgoing from depots
for d in range(0,number_depots):    
    for p in range(0,number_products):
        for t in range(0,number_time_periods):
            if t == 0:
                pf.addConstr(outgoing_depots[d*number_products*number_time_periods + p*number_time_periods + t] == 0)
            else:    
                link_number_start = number_suppliers*(number_depots + number_customers) + d*(number_depots - 1 + number_customers) + 1
                link_number_end = link_number_start + number_depots - 1 + number_customers
                total_outgoing = 0
                for element in range(link_number_start, link_number_end):
                    total_outgoing += products_shipped[(element-1)*number_products*number_time_periods + p*number_time_periods + t]
                pf.addConstr(outgoing_depots[d*number_products*number_time_periods + p*number_time_periods + t] == total_outgoing)

# incoming in depots
for d in range(0,number_depots): 
    target_depots = ["D"+str(d+1)]
    link_numbers = links.index[links["Destination"].isin(target_depots)].tolist()
    link_numbers_corrected = np.add(link_numbers, 1)
    durations = links.iloc[link_numbers,:].loc[:,"Duration"].tolist()
    print(link_numbers_corrected)
    print(durations)   
    for p in range(0,number_products):
        for t in range(0,number_time_periods):
            if t == 0:
                pf.addConstr(incoming_depots[d*number_products*number_time_periods + p*number_time_periods + t] == 0)
            else:
                total_incoming = 0
                counter = 0
                for element in link_numbers_corrected:
                    duration = durations[counter]
                    if duration > t:
                        pf.addConstr(incoming_depots[d*number_products*number_time_periods + p*number_time_periods + t] == total_incoming)
                        counter += 1
                        continue
                    else:
                        total_incoming += products_shipped[(element-1)*number_products*number_time_periods + p*number_time_periods + t - duration]
                    counter += 1
                pf.addConstr(incoming_depots[d*number_products*number_time_periods + p*number_time_periods + t] == total_incoming) 

# inventory level
for d in range(0,number_depots):    
    for p in range(0,number_products):
        for t in range(0,number_time_periods):
            if t == 0:
                pf.addConstr(inventory[d*number_products*number_time_periods + p*number_time_periods + t] == 0)
            else:    
                pf.addConstr(inventory[d*number_products*number_time_periods + p*number_time_periods + t] == inventory[d*number_products*number_time_periods + p*number_time_periods + t-1] - outgoing_depots[d*number_products*number_time_periods + p*number_time_periods + t] + incoming_depots[d*number_products*number_time_periods + p*number_time_periods + t])

# trucks arriving on a certain point in time
for l in range(0,number_links):
    link_duration = duration_link[l]
    for t in range(0,number_time_periods):
        if t < link_duration:
            pf.addConstr(arriving_trucks[l*number_time_periods + t] == 0)
            continue
        else:
            pf.addConstr(arriving_trucks[l*number_time_periods + t] == trucks_started[l*number_time_periods + t - link_duration ])

"""
# number of trucks on link
for l in range(0,number_links):
    for t in range(0,number_time_periods):
        if t == 0:
            pf.addConstr(trucks_present[l*number_time_periods + t] == 0)
        else:
            pf.addConstr(trucks_present[l*number_time_periods + t] == trucks_present[l*number_time_periods + t - 1] - arriving_trucks[l*number_time_periods + t] + trucks_started[l*number_time_periods + t])
"""

# cumulative number of product p produced at supplier s at time t
for s in range(0,number_suppliers):
    for p in range(0,number_products):
        for t in range(0,number_time_periods):
            total_demand_produced = 0
            link_number_start_suppliers = s*(number_depots + number_customers) + 1
            link_number_end_suppliers = link_number_start_suppliers + number_depots + number_customers
            for elem in (link_number_start_suppliers, link_number_end_suppliers):
                total_demand_produced += products_shipped[(elem-1)*number_products*number_time_periods + p*number_time_periods + t]
            pf.addConstr(total_shipped[s*number_products*number_time_periods + p*number_time_periods + t] == total_demand_produced)

# production constraints for minimum and maximum production
for s in range(0,number_suppliers):
    for p in range(0,number_products):
        df_helper_prod = production[((production["Supplier"] == "S"+str(s+1)) & (production["Product"] == "P"+str(p+1)))] 
        print(df_helper_prod)
        if df_helper_prod.empty:
            minimum_production = 0
            maximum_production = float("inf")
        else:
            minimum_production = df_helper_prod["Minimum"].values[0]
            maximum_production = df_helper_prod["Maximum"].values[0]
        print(minimum_production)
        print(maximum_production)  
        for t in range(0,number_time_periods):
            pf.addConstr(produced[s*number_products*number_time_periods + p*number_time_periods + t] * minimum_production <= total_shipped[s*number_products*number_time_periods + p*number_time_periods + t])
            pf.addConstr(total_shipped[s*number_products*number_time_periods + p*number_time_periods + t] <= produced[s*number_products*number_time_periods + p*number_time_periods + t] * maximum_production)

# transport possible if link is opened
for l in range(0,number_links):
    for p in range(0,number_products):
        for t in range(0,number_time_periods):
            pf.addConstr(products_shipped[l*number_products*number_time_periods + p*number_time_periods + t] <= M * link_opening[l])

# cumulative number of product p shipped from depot d at time t
for d in range(0,number_depots):
    for p in range(0,number_products):
        for t in range(0,number_time_periods):
            total_shipped_depot = 0
            link_number_start_depots = number_suppliers*(number_depots+number_customers)+d*(number_depots - 1 + number_customers) + 1
            link_number_end_depots = link_number_start_depots + number_depots - 1 + number_customers
            for elem in (link_number_start_suppliers, link_number_end_suppliers):
                total_shipped_depot += products_shipped[(elem-1)*number_products*number_time_periods + p*number_time_periods + t]
            pf.addConstr(total_shipped_depots[d*number_products*number_time_periods + p*number_time_periods + t] == total_shipped_depot)

# shipping from depot is limited by available inventory
for d in range(0,number_depots):
    for p in range(0,number_products):
        for t in range(0,number_time_periods):
            pf.addConstr(total_shipped_depots[d*number_products*number_time_periods + p*number_time_periods + t] <= inventory[p*number_depots*number_time_periods + d*number_time_periods + t])

# link capacities can only be positive if link is opened
for l in range(0,number_links):
    pf.addConstr(link_capacity[l] <= M * link_opening[l])

# number of trucks that start traveling on link is limited by link capacity
for l in range(0,number_links):
    for t in range(0,number_time_periods):
        pf.addConstr(trucks_started[l*number_time_periods + t] <= link_capacity[l])

# total product size at depot limited by depot capacity
for d in range(0,number_depots):
    for t in range(0,number_time_periods):
        total_stored = gb.LinExpr()
        for p in range(0,number_products):
            total_stored += inventory[p*number_depots*number_time_periods + d*number_time_periods + t] * product_size[p]
        pf.addConstr(total_stored <= capacity_depots[d])

"""
for p in range(0,number_products):
    total_stored_depot[d*number_time_periods + t] = gb.LinExpr()
    for d in range(0,number_depots):
        for t in range(0,number_time_periods):      
            total_stored_depot[d*number_time_periods + t] += inventory[p*number_depots*number_time_periods + d*number_time_periods + t] * product_size[p]

## Deze klopt nog niet vermoed ik ##

# products stored in depots is limited by depot size
for d in range(0,number_depots):
    for t in range(0,number_time_periods):
        pf.addConstr(total_stored_depot[d*number_time_periods + t] <= capacity_depots[d])
"""

# total product size transported limited by total truck capacity
for l in range(0,number_links):
    for t in range(0,number_time_periods):
        total_transported = gb.LinExpr()
        for p in range(0,number_products):
            total_transported += products_shipped[l*number_products*number_time_periods + p*number_time_periods + t] * product_size[p]
        pf.addConstr(total_transported <= trucks_started[l*number_time_periods + t] * truck_size)

for c in range(0,number_customers):
    link_numbers_customers = [number_depots+c]
    for s in range(1,number_suppliers):
        link_numbers_customers.append(s*(number_customers+number_depots) + number_depots + c)
    for p in range(0,number_products):
        for t in range(0,number_time_periods):
            summed = gb.LinExpr()
            for l in link_numbers_customers:
                for k in range(0,t+1):
                    summed += products_shipped[l*number_products*number_time_periods + p*number_time_periods + k]


        
pf.update()
pf.write("pf.lp")
pf.setParam('OutputFlag', 0)
pf.optimize()

print(pf.objval)

for l in range(number_links):
    if link_opening[l].X > 0:
        print(f"link {l} is opened")



