#%%
import pandas as pd
import numpy as np
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import mean_squared_error
import math 
import matplotlib.pyplot as plt
from statistics import mean
import warnings 
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.holtwinters import ExponentialSmoothing 
import time 
from math import sqrt
import datetime
from sklearn.ensemble import RandomForestRegressor
from sklearn import model_selection
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.tree import DecisionTreeRegressor, export_text
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.tree import plot_tree
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.preprocessing import MinMaxScaler
#%%

file = 'VbnData.xlsx'
sheet_name = 'Personen Rotterdam'

excel = pd.read_excel(file, sheet_name=sheet_name)

dates = excel["Date"]
data = excel['Demand'].values
print(data)

horizon = len(data)
significance = 1.96
percentage = 0.8

#Create a plot with the demand for Rotterdam between 2017 and 2023

plt.plot(dates, data, label='Demand')
plt.legend()
plt.title('Demand Individuals Rotterdam')
plt.xlabel('Date')
plt.ylabel('Demand')
plt.xticks(rotation=45)
plt.show()

rows = ['Individuen Landelijk', 'Huishoudens Landelijk', 'Individuen Rotterdam', 'Huishoudens Rotterdam']
columns = ['Current demand','1 LB', '1-period ahead', '1 UB', 'Change 1-period', 'Absolute change 1-period', '4 LB', '4-periods ahead', '4 UB', 'Change 4-periods', 'Absolute change 4-periods', '52 LB', '52-periods ahead', '52 UB','Change 52-periods', 'Absolute change 52-periods']

results = pd.DataFrame(index=rows, columns=columns)
 

#%%

print('INDIVIDUALS NATIONAL')

print('----------------------------------------')

########################

# HOLT

########################

file = 'VbnData.xlsx'

sheet_name = 'Personen Landelijk'

excel = pd.read_excel(file, sheet_name=sheet_name)

data = excel['Demand'].values

test_size = 1 #the number of periods you forecast ahead



data = data[test_size+7:]

train_index = int(len(data) * percentage) 

train = data[:train_index]

validation = data[train_index:]

val_length = len(validation)



start_time = time.time()



best_alpha = 0.844

best_beta = 0.544



forecast_val = []

residuals = []

if test_size == 1:

    history = [x for x in train]

else:

    history = train[: - test_size +1].tolist()

for t in range(0,min(test_size, val_length)):

    model = ExponentialSmoothing(history, trend='mul')

    model_fit = model.fit(smoothing_level=best_alpha, smoothing_trend=best_beta, optimized=False)

    yhat = model_fit.forecast(test_size)[-1]

    forecast_val.append(yhat)

    if (-(test_size-1)+ t) != 0:

        obs = train[-(test_size-1)+ t]

    else:

        obs = validation[0]

    history.append(obs)

    actual = validation[t]

    residual = yhat - actual

    residuals.append(residual)

for t in range(max(0,val_length-test_size)):

    model = ExponentialSmoothing(history, trend='mul')

    model_fit = model.fit(smoothing_level=best_alpha, smoothing_trend=best_beta, optimized=False)

    yhat = model_fit.forecast(test_size)[-1]

    forecast_val.append(yhat)

    obs = validation[t+1]

    history.append(obs)

    actual = validation[t]

    residual = yhat - actual

    residuals.append(residual)



RMSFE = np.sqrt(sum([x**2 for x in residuals]) / len(residuals))

band_size = significance*RMSFE



history = [x for x in data]

model = ExponentialSmoothing(history, trend='mul')

model_fit = model.fit(smoothing_level=best_alpha, smoothing_trend=best_beta, optimized=False)

forecast_test = model_fit.forecast(test_size)[-1]

LB = forecast_test - band_size

UB = forecast_test + band_size



end_time = time.time()

execution_time = end_time - start_time

change = ((forecast_test - data[-1]) / data[-1]) *100

ab = (forecast_test - data[-1])



print('Individuals National')

print('Current demand:', data[-1])

print(f'Forecast {test_size} periods ahead: {forecast_test}')

print('Lower Bound:', LB)  

print('Upper Bound:', UB)  

print('Optimal alpha:', best_alpha)  

print('Optimal beta:', best_beta) 

print(f"The HOLT method took {execution_time} seconds to execute.")



results.loc['Individuen Landelijk', '1-period ahead'] = forecast_test

results.loc['Individuen Landelijk', 'Current demand'] = data[-1]

results.loc['Individuen Landelijk', 'Change 1-period'] = change

results.loc['Individuen Landelijk', 'Absolute change 1-period'] = ab

results.loc['Individuen Landelijk', '1 LB'] = LB

results.loc['Individuen Landelijk', '1 UB'] = UB

print('----------------------------------------')

 