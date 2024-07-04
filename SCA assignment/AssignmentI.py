import time as pytime
import gurobipy as gb
import numpy as np
import pandas as pd
import re
import xarray as xr
import itertools as it
from sklearn.metrics.pairwise import euclidean_distances as euclid
import networkx as nx
import matplotlib.pyplot as plt
import os

os.chdir("C:\\Users\\dicod\\Documents\\python codes\\SCA assignment")

runtime_begin=pytime.time()

# Importing the data:
path="data_set_compl.xlsx"
SUPPLIERS = pd.read_excel(path, sheet_name="Suppliers")
DEPOTS = pd.read_excel(path, sheet_name="Depots")
CUSTOMERS = pd.read_excel(path, sheet_name="Customers")
PRODUCTS = pd.read_excel(path, sheet_name="Products")
LINKS = pd.read_excel(path, sheet_name="Links")
DEMAND = pd.read_excel(path, sheet_name="Demand")
BACKLOG = pd.read_excel(path, sheet_name="Backlog Penalty")
PRODUCTION = pd.read_excel(path, sheet_name="Production")
PARAMETERS = pd.read_excel(path, sheet_name="Parameters")

# Introducing sets:
supplier = SUPPLIERS["SupplierID"].tolist()
depot = DEPOTS["DepotID"].tolist()
customer = CUSTOMERS["CustomerID"].tolist()
product = PRODUCTS["ProductID"].tolist()

time_begin = int("".join(re.findall('[0-999]',PARAMETERS["Value"][1])))
time_end = int("".join(re.findall('[0-999]',PARAMETERS["Value"][2])))
time_char=re.sub('[0-9]',"",PARAMETERS["Value"][1])
time = [time_char+str(x) for x in range(time_begin,time_end+1)]
time_ext=['TIMEZERO']+time

depart = supplier + depot
arrive = depot + customer

supplen=len(supplier)
depolen=len(depot)
custlen=len(customer)
prodlen=len(product)
timelen=len(time)

H = time[-1]
M = 100000

# Defining given parameters:
gamma=PARAMETERS["Value"][0]
mult_backlog=10
mult_early_backlog = 0.5

h=xr.DataArray(DEPOTS['Holding Cost'].tolist(),dims=['depots'],coords={'depots':depot})
delta=xr.DataArray(DEPOTS['Capacity'].tolist(),dims=['depots'],coords={'depots':depot})
a=xr.DataArray(PRODUCTS['Size'].tolist(),dims=['products'],coords={'products':product})

u=xr.DataArray(np.zeros((supplen+depolen+custlen)),dims=['nodes'],coords={'nodes':supplier+depot+customer})
v=xr.DataArray(np.zeros((supplen+depolen+custlen)),dims=['nodes'],coords={'nodes':supplier+depot+customer})
for n in [SUPPLIERS,DEPOTS,CUSTOMERS]:
    for i in range(len(n)):
        u.loc[n.iloc[i,0]]=n.loc[i,'LocationX']
        v.loc[n.iloc[i,0]]=n.loc[i,'LocationY']

alpha=xr.DataArray(np.zeros((supplen,prodlen)),dims=['suppliers','products'],coords={'suppliers':supplier,'products':product})
beta=xr.DataArray(np.zeros((supplen,prodlen)),dims=['suppliers','products'],coords={'suppliers':supplier,'products':product})
for i in range(len(PRODUCTION)):
    row=PRODUCTION.loc[i,:]
    alpha.loc[row['Supplier'],row['Product']]=row['Minimum']
    beta.loc[row['Supplier'],row['Product']]=row['Maximum']

b=xr.DataArray(np.zeros((custlen,prodlen)),dims=['customers','products'],coords={'customers':customer,'products':product})
for i in range(len(BACKLOG)):
    row=BACKLOG.loc[i,:]
    b.loc[row['Customer'],row['Product']]=row['Amount']

o=xr.DataArray(M*np.ones((supplen+depolen,depolen+custlen)),dims=['departures','arrivals'],coords={'departures':depart,'arrivals':arrive})
capcost=xr.DataArray(np.zeros((supplen+depolen,depolen+custlen)),dims=['departures','arrivals'],coords={'departures':depart,'arrivals':arrive})
tau=xr.DataArray(np.zeros((supplen+depolen,depolen+custlen)),dims=['departures','arrivals'],coords={'departures':depart,'arrivals':arrive})
for i in range(len(LINKS)):
    row=LINKS.loc[i,:]
    o.loc[row['Origin'],row['Destination']]=row['Opening Cost']
    capcost.loc[row['Origin'],row['Destination']]=row['Capacity Cost']
    tau.loc[row['Origin'],row['Destination']]=row['Duration']

demand=xr.DataArray(np.zeros((custlen,prodlen,timelen)),dims=['customers','products','times'],coords={'customers':customer,'products':product,'times':time})
for i in range(len(DEMAND)):
    row=DEMAND.loc[i,:]
    demand.loc[row['Customer'],row['Product'],row['Time']]=row['Amount']

# The euclidean distance for nodes (supplier, depots and customers) with X-coor in u and Y-coor in v.
theta=xr.DataArray(euclid(np.column_stack((u,v))),dims=['dep_nodes','arr_nodes'],coords={'dep_nodes':supplier+depot+customer,'arr_nodes':supplier+depot+customer})

# Empty optimization model:
MILP = gb.Model()

# Decision variables:
# Binary
linkopen = MILP.addVars(depart,arrive, vtype=gb.GRB.BINARY, name='linkopen')
production = MILP.addVars(supplier, product, time, vtype=gb.GRB.BINARY, lb=0, ub=1, name='production')

# Integer
trucksdisp = MILP.addVars(depart, arrive, time, vtype=gb.GRB.INTEGER, lb=0, name='trucksdisp')
linkcap = MILP.addVars(depart, arrive, vtype=gb.GRB.INTEGER, lb=0, name='linkcap')

# Continuous nonnegative
shipped = MILP.addVars(depart, arrive, product, time, vtype=gb.GRB.CONTINUOUS, lb=0, name='shipped')
early = MILP.addVars(customer, product, time, vtype=gb.GRB.CONTINUOUS, lb=0, name='early')
late = MILP.addVars(customer, product, time, vtype=gb.GRB.CONTINUOUS, lb=0, name='late')
inv = MILP.addVars(product, depot, time_ext, vtype=gb.GRB.CONTINUOUS, lb=0, name='inv')

# Objective:
# Cost of opening link and procuring link capacity
cost1 = gb.quicksum(linkopen[i,j]*o.loc[i,j]+linkcap[i,j]*capcost.loc[i,j] for i,j in it.product(depart,arrive))

# Cost of Euclidean distance travel
cost2 = gb.quicksum(theta.loc[i,j]*trucksdisp[i,j,t] for i,j,t in it.product(depart,arrive,time))

# Holding costs
cost3 = gb.quicksum(h.loc[d]*a.loc[p]*inv[p,d,t] for p,d,t in it.product(product,depot,time))

# Costs of backlogs
cost4=gb.LinExpr()
for c in customer:
    for p in product:
        for t in time:
            if t != H:
                cost4 += b.loc[c,p]*(late[c,p,t]+mult_early_backlog*early[c,p,t])
            elif t == H:
                cost4 += mult_backlog*b.loc[c,p]*(late[c,p,t]+early[c,p,t])

costs=cost1+cost2+cost3+cost4
obj = gb.LinExpr()
obj += costs.values
MILP.setObjective(obj, gb.GRB.MINIMIZE)

# Constraints:
for p in product:
    for d in depot:
        for t in time_ext:
            if t=='TIMEZERO':
                MILP.addConstr(inv[p,d,t]==0)
            else:
                summed=gb.LinExpr()
                for i in depart:
                    time_ind=int(time.index(t)-tau.loc[i,d].values) # Determining the time index of 'time'-list at which items should be sent to arrive at time t
                    if time_ind>=0: # There can only be items incoming if the transportation time took shorter than current time since the initialization of the time horizon
                        summed+=shipped[i,d,p,time[time_ind]] 
                MILP.addConstr(inv[p,d,t]-inv[p,d,tmin1]+gb.quicksum(shipped[d,j,p,t] for j in arrive)==summed) # The inventory constraint
            tmin1=t # In next iteration, t represents the previous time label, denoted here by tmin1: used to acces previous time inventory level

# If there is production of product p at supplier s at time t, make sure that the output is in between the min and max capacity
for s in supplier:
    for p in product:
        for t in time:
            MILP.addConstr(production[s,p,t]*alpha.loc[s,p]<=gb.quicksum(shipped[s,j,p,t] for j in arrive))
            MILP.addConstr(production[s,p,t]*beta.loc[s,p]>=gb.quicksum(shipped[s,j,p,t] for j in arrive))

# Transport only possible if link is opened
for i in depart:
    for j in arrive:
        for p in product:
            for t in time:
                MILP.addConstr(shipped[i,j,p,t]<=M*linkopen[i,j])

"""
# Shipments out of a depot bounded by available inventory
for p in product:
    for d in depot:
        for t in time:
            MILP.addConstr(gb.quicksum(shipped[d,j,p,t] for j in arrive)<= inv[p,d,t])
"""
for i in depart:
    for j in arrive:
        MILP.addConstr(linkcap[i,j]<=M*linkopen[i,j]) # Link capacity can only be procured if the link is first opened
        for t in time:
            MILP.addConstr(trucksdisp[i,j,t]<=linkcap[i,j]) # Amount of trucks contrained at the procured link capacity per time period

# Volume of product in depots may not exceed depot size capacity
for d in depot:
    for t in time:
        MILP.addConstr(gb.quicksum(inv[p,d,t]*a.loc[p] for p in product)<=delta.loc[d])

# Volume of products in trucks may not exceed truck capacity
for i in depart:
    for j in arrive:
        for t in time:
            MILP.addConstr(gb.quicksum(shipped[i,j,p,t]*a.loc[p] for p in product)<=gamma*trucksdisp[i,j,t])

for c in customer:
    for p in product:
        for t in time:
            cumdif=0
            for k in time[:time.index(t)+1]:
                summed=gb.LinExpr()
                for i in depart:
                        time_ind=int(time.index(k)-tau.loc[i,c].values) # Determining the time index of 'time'-list at which items should be sent to arrive at time k
                        if time_ind>=0: # There can only be items incoming if the transportation time took shorter than current time since the initialization of the time horizon
                            summed+=shipped[i,c,p,time[time_ind]]
                cumdif +=summed-demand.loc[c,p,k]

            MILP.addConstr(cumdif<=early[c,p,t])
            MILP.addConstr(-cumdif<=late[c,p,t])

# Generating the model
MILP.update()

# Writing the model to a text file
MILP.write("MILP.lp")

# Omitting intermediate output
MILP.setParam('OutputFlag', 0)

# Optimizing the model
opttime_begin=pytime.time()
MILP.optimize()
opttime_end=pytime.time()

# Writing results to dataFrame
col=['Variable:']+time
results=pd.DataFrame(np.zeros((1,len(time)+1)),columns=col)

for s in supplier:
    for p in product:
        if any([linkopen[s,j].X for j in arrive]):
            results=pd.concat([results,pd.DataFrame([['Prod.: {}-{}'.format(s,p)]+[int(production[s,p,t].X) for t in time]],columns=col)],ignore_index=True)

for d in depot:
    for p in product:
        if any([linkopen[d,j].X for j in arrive]) or any([linkopen[i,d].X for i in depart]):
            results=pd.concat([results,pd.DataFrame([['Inv.: {}-{}'.format(d,p)]+[round(inv[p,d,t].X,2) for t in time]],columns=col)],ignore_index=True)

for c in customer:
    for p in product:
        results=pd.concat([results,pd.DataFrame([['Early: {}-{}'.format(c,p)]+[round(early[c,p,t].X,2) for t in time]],columns=col)],ignore_index=True)
        results=pd.concat([results,pd.DataFrame([['Late: {}-{}'.format(c,p)]+[round(late[c,p,t].X,2) for t in time]],columns=col)],ignore_index=True)

for i in depart:
    for j in arrive:
        if linkopen[i,j].X>0:
            for p in product:
                if p==product[-1]:
                    results=pd.concat([results,pd.DataFrame([['Shipm.: {}-{}'.format(i,j)]+['{} (#truck={})'.format(round(shipped[i,j,p,t].X,2), trucksdisp[i,j,t].X) if shipped[i,j,p,t].X>0 else str(0) for t in time]],columns=col)],ignore_index=True)
                else:
                    results=pd.concat([results,pd.DataFrame([['Shipm.: {}-{}'.format(i,j)]+[round(shipped[i,j,p,t].X,2) if shipped[i,j,p,t].X>0 else 0 for t in time]],columns=col)],ignore_index=True)
results=results.drop(index=0)

# Making visual representation of optimal network with link capacities:
G=nx.Graph()
G.add_nodes_from(supplier+depot+customer)
G.add_edges_from([tuple((i,j,{'weight':int(linkcap[i,j].X)})) for i,j in it.product(depart,arrive) if linkopen[i,j].X>0])
points=[[n,tuple((float(u.loc[n].values),float(v.loc[n].values)))] for n in supplier+depot+customer]
pos = {name: point for name,point in points}

colormap=supplen*['yellow']+depolen*['red']+custlen*['green']
fig, ax = plt.subplots()
nx.draw(G, pos=pos, node_color=colormap, node_size=600, ax=ax,with_labels=True)
nx.draw_networkx_labels(G, pos=pos)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)
plt.axis("on")
plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
plt.title('Visualization of model optimal supply network with link capacities')
ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
plt.show()

opt_time=opttime_end-opttime_begin
runtime_end=pytime.time()
runtime=runtime_end-runtime_begin
timedf=pd.DataFrame([['Overal cost objective',MILP.objVal],['Total file runtime',runtime],['Gurobi model opt. time',opt_time]],columns=[time[0],time[1]])
results=pd.concat([results,timedf],ignore_index=True)
results.to_excel('ModelOutput.xlsx',index=False)

# cost1_check = 0
# for i,j in it.product(depart,arrive):
#     cost1_check += linkopen[i,j].X*o.loc[i,j].values+linkcap[i,j].X*capcost.loc[i,j].X
