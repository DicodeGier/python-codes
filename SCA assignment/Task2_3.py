import gurobipy as gb
import numpy as np
import pandas as pd
import re
import time as pytime
import xarray as xr
import itertools as it
from sklearn.metrics.pairwise import euclidean_distances as euclid
import networkx as nx
import matplotlib.pyplot as plt
from copy import deepcopy as deepc
import os

class Run:
    def __init__(self,path):
        self.total_opttime=0
        # Importing the data:
        SUPPLIERS = pd.read_excel(path, sheet_name="Suppliers")
        DEPOTS = pd.read_excel(path, sheet_name="Depots")
        CUSTOMERS = pd.read_excel(path, sheet_name="Customers")
        PRODUCTS = pd.read_excel(path, sheet_name="Products")
        LINKS = pd.read_excel(path, sheet_name="Links")
        DEMAND = pd.read_excel(path, sheet_name="Demand")
        BACKLOG = pd.read_excel(path, sheet_name="Backlog Penalty")
        PRODUCTION = pd.read_excel(path, sheet_name="Production")
        PARAMETERS = pd.read_excel(path, sheet_name="Parameters")
        CORRELATION = pd.read_excel(path,sheet_name="Correlation")

        # Introducing sets:
        self.supplier = SUPPLIERS["SupplierID"].tolist()
        self.depot = DEPOTS["DepotID"].tolist()
        self.customer = CUSTOMERS["CustomerID"].tolist()
        self.product = PRODUCTS["ProductID"].tolist()

        time_begin = int("".join(re.findall('[0-999]',PARAMETERS["Value"][1])))
        time_end = int("".join(re.findall('[0-999]',PARAMETERS["Value"][2])))
        time_char=re.sub('[0-9]',"",PARAMETERS["Value"][1])
        self.time = [time_char+str(x) for x in range(time_begin,time_end+1)]
        self.time_ext=['TIMEZERO']+self.time

        self.supplen=len(self.supplier)
        self.depolen=len(self.depot)
        self.custlen=len(self.customer)
        self.prodlen=len(self.product)
        self.timelen=len(self.time)

        self.depart = self.supplier + self.depot
        self.arrive = self.depot + self.customer
        self.H = self.time[-1]
        self.M = 100000

        #Defining given parameters
        self.gamma=PARAMETERS["Value"][0]
        self.mult_backlog=10
        self.mult_early_backlog=0.5

        self.h=xr.DataArray(DEPOTS['Holding Cost'].tolist(),dims=['depots'],coords={'depots':self.depot})
        self.delta=xr.DataArray(DEPOTS['Capacity'].tolist(),dims=['depots'],coords={'depots':self.depot})
        self.a=xr.DataArray(PRODUCTS['Size'].tolist(),dims=['products'],coords={'products':self.product})

        self.u=xr.DataArray(np.zeros((self.supplen+self.depolen+self.custlen)),dims=['nodes'],coords={'nodes':self.supplier+self.depot+self.customer})
        self.v=xr.DataArray(np.zeros((self.supplen+self.depolen+self.custlen)),dims=['nodes'],coords={'nodes':self.supplier+self.depot+self.customer})
        for n in [SUPPLIERS,DEPOTS,CUSTOMERS]:
            for i in range(len(n)):
                self.u.loc[n.iloc[i,0]]=n.loc[i,'LocationX']
                self.v.loc[n.iloc[i,0]]=n.loc[i,'LocationY']

        self.availrate=xr.DataArray(np.zeros((self.supplen,self.prodlen)),dims=['suppliers','products'],coords={'suppliers':self.supplier,'products':self.product})
        self.beta=xr.DataArray(np.zeros((self.supplen,self.prodlen)),dims=['suppliers','products'],coords={'suppliers':self.supplier,'products':self.product})
        for i in range(len(PRODUCTION)):
            row=PRODUCTION.loc[i,:]
            self.availrate.loc[row['Supplier'],row['Product']]=row['Availability Rate']
            self.beta.loc[row['Supplier'],row['Product']]=row['Maximum']

        self.b=xr.DataArray(np.zeros((self.custlen,self.prodlen)),dims=['customers','products'],coords={'customers':self.customer,'products':self.product})
        for i in range(len(BACKLOG)):
            row=BACKLOG.loc[i,:]
            self.b.loc[row['Customer'],row['Product']]=row['Amount']

        self.o=xr.DataArray(self.M*np.ones((self.supplen+self.depolen,self.depolen+self.custlen)),dims=['departures','arrivals'],coords={'departures':self.depart,'arrivals':self.arrive})
        self.capcost=xr.DataArray(np.zeros((self.supplen+self.depolen,self.depolen+self.custlen)),dims=['departures','arrivals'],coords={'departures':self.depart,'arrivals':self.arrive})
        self.tau=xr.DataArray(np.zeros((self.supplen+self.depolen,self.depolen+self.custlen)),dims=['departures','arrivals'],coords={'departures':self.depart,'arrivals':self.arrive})
        for i in range(len(LINKS)):
            row=LINKS.loc[i,:]
            self.o.loc[row['Origin'],row['Destination']]=row['Opening Cost']
            self.capcost.loc[row['Origin'],row['Destination']]=row['Capacity Cost']
            self.tau.loc[row['Origin'],row['Destination']]=row['Duration']

        self.demand_mu=xr.DataArray(np.zeros((self.custlen,self.prodlen,self.timelen)),dims=['customers','products','times'],coords={'customers':self.customer,'products':self.product,'times':self.time})
        self.demand_sigma=xr.DataArray(np.zeros((self.custlen,self.prodlen,self.timelen)),dims=['customers','products','times'],coords={'customers':self.customer,'products':self.product,'times':self.time})
        for i in range(len(DEMAND)):
            row=DEMAND.loc[i,:]
            self.demand_mu.loc[row['Customer'],row['Product'],row['Time']]=row['Expected Amount']
            self.demand_sigma.loc[row['Customer'],row['Product'],row['Time']]=row['Standard Deviation']
        
        #The euclidean distance for nodes (supplier, depots and customers) with X-coor in u and Y-coor in v.
        self.theta=xr.DataArray(euclid(np.column_stack((self.u,self.v))),dims=['dep_nodes','arr_nodes'],coords={'dep_nodes':self.supplier+self.depot+self.customer,'arr_nodes':self.supplier+self.depot+self.customer})

        self.correlat=xr.DataArray(np.zeros((self.custlen,self.prodlen,self.prodlen)),dims=['customer','product1','product2'],coords={'customer':self.customer,'product1':self.product,'product2':self.product})
        for i in range(len(CORRELATION)):
            row=CORRELATION.loc[i,:]
            self.correlat.loc[row['Customer'],row[1],row[2]]=row['Correlation']
            self.correlat.loc[row['Customer'],row[2],row[1]]=row['Correlation'] # Correlation matrix is symmetric

        for c,p in it.product(self.customer,self.product):
            self.correlat.loc[c,p,p]=1 #Diagonal elements correlate perfectly

    def scenariocreation(self,nofsets,stratreturn=False,usestratsol=False,lnko_inR=None,lnkcap_inR=None,lnko_inM=None,lnkcap_inM=None,USEMEANS=False):
        res_list_R=np.zeros((nofsets))
        res_list_M=np.zeros((nofsets))

        for l in range(nofsets):
            # Make copy of standard model to add the constraints that involve the uncertain parameters
            # If usestratsol=True, then for Task 2 and Task 3 the same scenarios are used to the Random and Mean network inputted
            model_R=self.model.copy()
            model_R.update()

            if usestratsol:
                model_M=self.model.copy()
                model_M.update()

            if USEMEANS:
                self.disrupt=xr.DataArray(self.availrate.values.reshape((self.scenlen,self.supplen,self.prodlen)),dims=['scenario','supplier','product'],coords={'scenario':self.scenario,'supplier':self.supplier,'product':self.product}).expand_dims(dim={'time':self.time})
                self.realdem=xr.DataArray(self.demand_mu.values.reshape((self.scenlen,self.custlen,self.prodlen,self.timelen)),dims=['scenario','customer','product','time'],coords={'scenario':self.scenario,'customer':self.customer,'product':self.product,'time':self.time})
            else:
                #Scenario creation:
                self.disrupt =xr.DataArray(np.zeros((self.timelen,self.scenlen,self.supplen,self.prodlen)),dims=['time','scenario','supplier','product'],coords={'time':self.time,'scenario':self.scenario,'supplier':self.supplier,'product':self.product})
                for t in self.time:
                    self.disrupt.loc[t,self.scenario,self.supplier,self.product]=np.random.binomial(n=1,p=self.availrate,size=(self.scenlen,self.supplen,self.prodlen))
                
                self.realdem=xr.DataArray(np.zeros((self.scenlen,self.custlen,self.prodlen,self.timelen)),dims=['scenario','customer','product','time'],coords={'scenario':self.scenario,'customer':self.customer,'product':self.product,'time':self.time})
                for c in self.customer:
                    for t in self.time:
                        sigmas=np.diag(self.demand_sigma.loc[c,self.product,t].values)
                        covmat=np.matmul(np.matmul(sigmas,self.correlat.loc[c,self.product,self.product].values),sigmas)
                        for sc in self.scenario:
                            self.realdem.loc[sc,c,self.product,t]=np.random.multivariate_normal(mean=self.demand_mu.loc[c,self.product,t].values,cov=covmat)

            # Constrainsts for early and late are added 
            for sc,c,p in it.product(self.scenario,self.customer,self.product):    
                for t in self.time:
                    cumdif=0
                    cumdif_m=0
                    for k in self.time[:self.time.index(t)+1]:
                        summed=gb.LinExpr()
                        summed_m=gb.LinExpr()
                        for i in self.depart:
                                time_ind=int(self.time.index(k)-self.tau.loc[i,c].values) # Determining the time index of 'time'-list at which items should be sent to arrive at time k
                                if time_ind>=0: # There can only be items incoming if the transportation time took shorter than current time since the initialization of the time horizon
                                    summed+=model_R.getVarByName('shipped[{},{},{},{},{}]'.format(str(sc),str(i),str(c),str(p),str(self.time[time_ind]))) #self.shipped[sc,i,c,p,self.time[time_ind]]
                                    if usestratsol:
                                        summed_m+=model_M.getVarByName('shipped[{},{},{},{},{}]'.format(str(sc),str(i),str(c),str(p),str(self.time[time_ind]))) #self.shipped[sc,i,c,p,self.time[time_ind]]
                        cumdif +=summed-self.realdem.loc[sc,c,p,k].values
                        if usestratsol:
                            cumdif_m+=summed_m-self.realdem.loc[sc,c,p,k].values

                    model_R.addConstr(cumdif<=model_R.getVarByName('early[{},{},{},{}]'.format(str(sc),str(c),str(p),str(t)))) #self.early[sc,c,p,t])
                    model_R.addConstr(-cumdif<=model_R.getVarByName('late[{},{},{},{}]'.format(str(sc),str(c),str(p),str(t)))) #self.late[sc,c,p,t])
                    if usestratsol:
                        model_M.addConstr(cumdif_m<=model_M.getVarByName('early[{},{},{},{}]'.format(str(sc),str(c),str(p),str(t)))) #self.early[sc,c,p,t])
                        model_M.addConstr(-cumdif_m<=model_M.getVarByName('late[{},{},{},{}]'.format(str(sc),str(c),str(p),str(t)))) #self.late[sc,c,p,t])

            # Constraints for production are added
            [model_R.addConstr(self.disrupt.loc[t,sc,s,p].values*model_R.getVarByName('production[{},{},{},{}]'.format(str(sc),str(s),str(p),str(t),))*self.beta.loc[s,p].values>=gb.quicksum(model_R.getVarByName('shipped[{},{},{},{},{}]'.format(str(sc),str(s),str(j),str(p),str(t))) for j in self.arrive)) for sc,s,p,t in it.product(self.scenario,self.supplier,self.product,self.time)]

            if usestratsol:
                [model_M.addConstr(self.disrupt.loc[t,sc,s,p].values*model_M.getVarByName('production[{},{},{},{}]'.format(str(sc),str(s),str(p),str(t),))*self.beta.loc[s,p].values>=gb.quicksum(model_M.getVarByName('shipped[{},{},{},{},{}]'.format(str(sc),str(s),str(j),str(p),str(t))) for j in self.arrive)) for sc,s,p,t in it.product(self.scenario,self.supplier,self.product,self.time)]

                [model_R.addConstr(model_R.getVarByName('linkopen[{},{}]'.format(str(i),str(j)))==lnko_inR.loc[i,j].values) for i,j in it.product(self.depart,self.arrive)]
                [model_R.addConstr(model_R.getVarByName('linkcap[{},{}]'.format(str(i),str(j)))==lnkcap_inR.loc[i,j].values) for i,j in it.product(self.depart,self.arrive)]
                [model_M.addConstr(model_M.getVarByName('linkopen[{},{}]'.format(str(i),str(j)))==lnko_inM.loc[i,j].values) for i,j in it.product(self.depart,self.arrive)]
                [model_M.addConstr(model_M.getVarByName('linkcap[{},{}]'.format(str(i),str(j)))==lnkcap_inM.loc[i,j].values) for i,j in it.product(self.depart,self.arrive)]
            
            # Optimizing the model
            opttime_begin=pytime.time()
            model_R.update()
            model_R.optimize()
            if usestratsol:
                model_M.update()
                model_M.optimize()
            opttime_end=pytime.time()
            self.total_opttime+=(opttime_end-opttime_begin)
            res_list_R[l]=round(model_R.ObjVal,2)
            if usestratsol:
                res_list_M[l]=round(model_M.ObjVal,2)
            #print([res_list_R[l],res_list_M[l],opttime_end-opttime_begin,self.total_opttime])
            print(l)
            
        if stratreturn:
            lnko_out=xr.DataArray(np.zeros((self.supplen+self.depolen,self.depolen+self.custlen)),dims=['departures','arrivals'],coords={'departures':self.depart,'arrivals':self.arrive})
            lnkcap_out=xr.DataArray(np.zeros((self.supplen+self.depolen,self.depolen+self.custlen)),dims=['departures','arrivals'],coords={'departures':self.depart,'arrivals':self.arrive})
            for i in self.depart:
                for j in self.arrive:
                    lnko_out.loc[i,j]=model_R.getVarByName('linkopen[{},{}]'.format(str(i),str(j))).X
                    lnkcap_out.loc[i,j]=model_R.getVarByName('linkcap[{},{}]'.format(str(i),str(j))).X 
            return res_list_R,lnko_out,lnkcap_out
        elif usestratsol:
            return res_list_R,res_list_M
        else:
            return res_list_R

    def initialmodel(self,scenlen):
        self.scenlen=scenlen
        self.scenario=['SCEN'+str(w) for w in range(1,1+self.scenlen)]
        # Empty optimization model:
        MILP = gb.Model()

        # Variables:
        # Binary
        linkopen = MILP.addVars(self.depart,self.arrive, vtype=gb.GRB.BINARY, name='linkopen')
        production = MILP.addVars(self.scenario,self.supplier,self.product,self.time, vtype=gb.GRB.BINARY, lb=0, ub=1, name='production')

        # Instead of integer, continuous values are now allowed
        trucksdisp = MILP.addVars(self.scenario,self.depart, self.arrive, self.time, vtype=gb.GRB.CONTINUOUS, lb=0, name='trucksdisp')
        linkcap = MILP.addVars(self.depart, self.arrive, vtype=gb.GRB.CONTINUOUS, lb=0, name='linkcap')

        # Continuous nonnegative
        shipped = MILP.addVars(self.scenario,self.depart, self.arrive, self.product, self.time, vtype=gb.GRB.CONTINUOUS, lb=0, name='shipped')
        early = MILP.addVars(self.scenario,self.customer, self.product, self.time, vtype=gb.GRB.CONTINUOUS, lb=0, name='early')
        late = MILP.addVars(self.scenario,self.customer,self.product, self.time, vtype=gb.GRB.CONTINUOUS, lb=0, name='late')
        inv = MILP.addVars(self.scenario,self.product, self.depot, self.time_ext, vtype=gb.GRB.CONTINUOUS, lb=0, name='inv')
        
        # Objective:
        # Cost of opening link and procuring link capacity
        cost1 = gb.quicksum(linkopen[i,j]*self.o.loc[i,j]+linkcap[i,j]*self.capcost.loc[i,j] for i,j in it.product(self.depart,self.arrive))

        # Cost of Euclidean distance travel
        cost2 = gb.quicksum(self.theta.loc[i,j]*trucksdisp[sc,i,j,t] for sc,i,j,t in it.product(self.scenario,self.depart,self.arrive,self.time))

        # Holding costs
        cost3 = gb.quicksum(self.h.loc[d]*self.a.loc[p]*inv[sc,p,d,t] for sc,p,d,t in it.product(self.scenario,self.product,self.depot,self.time))

        # Costs of backlogs
        cost4=gb.LinExpr()
        for c,p,sc,t in it.product(self.customer,self.product,self.scenario,self.time):
            if t != self.H:
                cost4 += self.b.loc[c,p]*(late[sc,c,p,t]+self.mult_early_backlog*early[sc,c,p,t])
            elif t == self.H:
                cost4 += self.mult_backlog*self.b.loc[c,p]*(late[sc,c,p,t]+early[sc,c,p,t])

        costs=cost1+(cost2+cost3+cost4)/self.scenlen
        obj = gb.LinExpr()
        obj += costs.values
        MILP.setObjective(obj, gb.GRB.MINIMIZE)

        # Constraints:
        for sc,p,d in it.product(self.scenario,self.product,self.depot):
            for t in self.time_ext:
                if t=='TIMEZERO':
                    MILP.addConstr(inv[sc,p,d,t]==0)
                else:
                    summed=gb.LinExpr()
                    for i in self.depart:
                        time_ind=int(self.time.index(t)-self.tau.loc[i,d].values) # Determining the time index of 'time'-list at which items should be sent to arrive at time t
                        if time_ind>=0: # There can only be items incoming if the transportation time took shorter than current time since the initialization of the time horizon
                            summed+=shipped[sc,i,d,p,self.time[time_ind]] 
                    MILP.addConstr(inv[sc,p,d,t]-inv[sc,p,d,tmin1]+gb.quicksum(shipped[sc,d,j,p,t] for j in self.arrive)==summed) # The inventory constraint
                tmin1=t # In next iteration, t represents the previous time label, denoted here by tmin1: used to acces previous time inventory level

        #Transport only possible if link is opened
        [MILP.addConstr(shipped[sc,i,j,p,t]<=self.M*linkopen[i,j]) for sc,i,j,p,t in it.product(self.scenario,self.depart,self.arrive,self.product,self.time)]

        # Link capacity can only be procured if the link is first opened
        [MILP.addConstr(linkcap[i,j]<=self.M*linkopen[i,j]) for i,j in it.product(self.depart,self.arrive)]

        # Amount of trucks contrained at the procured link capacity per time period
        [MILP.addConstr(trucksdisp[sc,i,j,t]<=linkcap[i,j]) for i,j,t,sc in it.product(self.depart,self.arrive,self.time,self.scenario)] 

        # Volume of product in depots may not exceed depot size capacity
        [MILP.addConstr(gb.quicksum(inv[sc,p,d,t]*self.a.loc[p] for p in self.product)<=self.delta.loc[d]) for sc,d,t in it.product(self.scenario,self.depot,self.time)]

        # Volume of products in trucks may not exceed truck capacity
        [MILP.addConstr(gb.quicksum(shipped[sc,i,j,p,t]*self.a.loc[p] for p in self.product)<=self.gamma*trucksdisp[sc,i,j,t]) for i,j,t,sc in it.product(self.depart,self.arrive,self.time,self.scenario)]

        # Generating the model
        MILP.update()
        MILP.setParam('OutputFlag', 0)
        self.model=MILP

# please change the directory to the file "uncertainty_data_set.xlsx"
os.chdir("C:\\Users\\dicod\\Documents\\python codes\\SCA assignment")        

runtime_begin=pytime.time()

# Choose the number of scenarios for each scenario set
scenl=100

# Creating instance entailing reading the excel file and extracting the parameters to attributes of the instance
inst=Run(path="uncertainty_data_set.xlsx")
singlinst=deepc(inst)

inst.initialmodel(scenlen=scenl)
singlinst.initialmodel(scenlen=1)

# Vector of SAA solutions of length 'nofsets' where each scenario set contains 'scenlen' number of scenarios
# res_list=inst.scenariocreation(nofsets=10)

# The SAA optimal network as first solution of task 2. The same solution can be used to determine the optimal set of links with their capacities (see line thereafter)
runtime_begin_2 = pytime.time()
objvalSAAR,lnko_outR,lnkcap_outR=inst.scenariocreation(nofsets=1,stratreturn=True)
runtime_end_2 = pytime.time()
total_runtime_2 = runtime_end_2 - runtime_begin_2
opttime_2 = inst.total_opttime
print(total_runtime_2, opttime_2)
runtime_begin_3 = pytime.time()
objvalSAAM,lnko_outM,lnkcap_outM=singlinst.scenariocreation(nofsets=1,stratreturn=True,USEMEANS=True)
runtime_end_3 = pytime.time()
total_runtime_3 = runtime_end_3 - runtime_begin_3
opttime_3 = singlinst.total_opttime
print(total_runtime_3, opttime_3)

res_list=inst.scenariocreation(nofsets=10)
# The optimal network is then inputted to several separate scenarios: when scenlen=1, number of sets correspond to a single scenario each time
lstR,lstM=singlinst.scenariocreation(nofsets=scenl,usestratsol=True,lnko_inR=lnko_outR,lnkcap_inR=lnkcap_outR,lnko_inM=lnko_outM,lnkcap_inM=lnkcap_outM)

runtime_end=pytime.time()
total_runtime=runtime_end-runtime_begin
overallres=pd.DataFrame([[float(objvalSAAR)],[float(objvalSAAM)],res_list,lstR,lstM,[total_runtime],[inst.total_opttime]],
                        index=['The optimal SAA objective value R','The optimal SAA objective value M','Vector of SAA objective values','Vector of Objective values for separate scenarios R','Vector of Objective values for separate scenarios M','Total runtime', 'Total Gurobi optimizing time'])
overallres.to_excel('OutputTask2_3.xlsx')

# Making visual representation of optimal network with link capacities:
G=nx.Graph()
font = {'size':24}
plt.rc('font',**font)

G.add_nodes_from(inst.supplier+inst.depot+inst.customer)
G.add_edges_from([tuple((i,j,{'weight':round(float(lnkcap_outR.loc[i,j].values),2)})) for i,j in it.product(inst.depart,inst.arrive) if lnko_outR.loc[i,j].values>0])
points=[[n,tuple((float(inst.u.loc[n].values),float(inst.v.loc[n].values)))] for n in inst.supplier+inst.depot+inst.customer]
pos = {name: point for name,point in points}

colormap=inst.supplen*['yellow']+inst.depolen*['red']+inst.custlen*['green']
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

# Making visual representation of optimal network with link capacities:
G=nx.Graph()
font = {'size':24}
plt.rc('font',**font)

G.add_nodes_from(singlinst.supplier+singlinst.depot+singlinst.customer)
G.add_edges_from([tuple((i,j,{'weight':round(float(lnkcap_outM.loc[i,j].values),2)})) for i,j in it.product(singlinst.depart,singlinst.arrive) if lnko_outM.loc[i,j].values>0])
points=[[n,tuple((float(singlinst.u.loc[n].values),float(singlinst.v.loc[n].values)))] for n in singlinst.supplier+singlinst.depot+singlinst.customer]
pos = {name: point for name,point in points}

colormap=singlinst.supplen*['yellow']+singlinst.depolen*['red']+singlinst.custlen*['green']
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
