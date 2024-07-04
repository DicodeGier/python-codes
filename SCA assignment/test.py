import gurobipy as gb
list = ['S1D1', 'S1C1', 'D1C1']

MIQP = gb.Model()
links = MIQP.addVars(list, vtype=gb.GRB.INTEGER, lb=0, name='links')
print(links)