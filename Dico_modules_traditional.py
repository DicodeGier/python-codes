#%%
#test test test
# test 2
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
from sklearn.metrics import r2_score


#%%
file = 'VbnData.xlsx'
sheet_name = 'Personen Rotterdam'
excel = pd.read_excel(file, sheet_name=sheet_name)
dates = excel["Date"]
data = excel['Demand'].values
horizon = len(data)

# Define the number of splits
test_size = 4  #the number of periods you want to forecast ahead
test_set_length = 20
n_splits = 8

percentage = 100/120 

# remove observations such that the traditional and ML methods operate on the same data
data = data[test_size+7:]
dates = dates[test_size+7:].reset_index(drop=True)

tscv = TimeSeriesSplit(n_splits=n_splits, test_size=test_set_length, max_train_size=100+20)  

for i, (train_index, test_index) in enumerate(tscv.split(data)):
    print(f"Fold {i}:")
    print(f"  Train: index={train_index}")
    print(f"  Test:  index={test_index}")

# Initialize lists to store train, validation, and test observations
train = [] 
validation = []
test = []

# Loop over the splits and store the train, validation, and test observations
for train_index, test_index in tscv.split(data):
    train_data, test_data = data[train_index], data[test_index]
    
    validation_index = int(len(train_data) * percentage)  # 80% of train data
    train.append(train_data[:validation_index])
    validation.append(train_data[validation_index:])
    test.append(test_data)

# Print the lengths of train, validation, and test sets
for i in range(n_splits):
    print(f"Split {i+1}:")
    print(f"Train: {len(train[i])} observations")
    print(f"Validation: {len(validation[i])} observations")
    print(f"Test: {len(test[i])} observations")
    print()


# Plotting the train, validation, and test indices    
fig, ax = plt.subplots()
for i, (train_index, test_index) in enumerate(tscv.split(data)):
    train_dates = dates[train_index]
    validation_dates = dates[train_index[-test_set_length:]]  
    test_dates = dates[test_index]
    fold_number = i + 1

    ax.plot(train_dates, [fold_number] * len(train_dates), c='blue', label=f'Fold {fold_number} (Train)')
    ax.plot(validation_dates, [fold_number] * len(validation_dates), c='green', label=f'Fold {fold_number} (Validation)')
    ax.plot(test_dates, [fold_number] * len(test_dates), c='red', label=f'Fold {fold_number} (Test)')

ax.set_yticks(range(1, n_splits + 1))
ax.legend(["Train", "Validation", "Test"], loc='lower right')

plt.xlabel('Date')
plt.ylabel('Fold number')
plt.xticks(rotation=45)
plt.show()

#%%
########################
# Naive forecasting 
# ONLY ONE PERIOD
########################
start_time = time.time()

if test_size == 1:
    
    rmse_all = []
    forecast_all = []
    test_all = []
    test_indices = []

    for fold, (train_index, test_index) in enumerate(tscv.split(data), 1):
        train = []
        validation = []
        test = []
        trainval_data, test_data = data[train_index].tolist(), data[test_index].tolist()
        test.extend(test_data)
        test_indices.extend(test_index)
    
        validation_index = int(len(trainval_data) * percentage) 
        train.extend(trainval_data[:validation_index])
        validation.extend(trainval_data[validation_index:])
    
        train_length = len(train)
        val_length = len(validation)
        test_length = len(test)
        trainval_length = len(trainval_data)
    
       #No hyper-parameters so no validation necessary
        
        # Initialize y_1_hat with the last observation of the validation set
        y_1_hat = validation[-1]
    
        # Perform naive forecasting for the test set
        forecast_test = [y_1_hat]
        
        for t in range(test_set_length-1):
            prediction = test[t]
            forecast_test.append(prediction)
             
        forecast_all.extend(forecast_test)
        test_all.extend(test)     
        mse_test = mean_squared_error(test, forecast_test)
        rmse_test = math.sqrt(mse_test)
        rmse_all.append(rmse_test)
    
    resulting_rmse = mean(rmse_all)
    forecast_array = np.array(forecast_all)
    test_array = np.array(test_all)

    result = abs(forecast_array - test_array)
    MAE = sum(result) / len(result)
    print("MAE:", MAE)
    
    r_squared = r2_score(test_array, forecast_array)
    print("R-squared:", r_squared)

    print("RMSE Naive", test_size, "periods ahead forecasting:", resulting_rmse) 

    fig, ax = plt.subplots()
    test_dates = dates[test_indices] 
    ax.plot(test_dates, test_all, label='Test Observations')
    ax.plot(test_dates, forecast_all, label='Naive Forecast')
    
    ax.legend()
    plt.xlabel('Date')
    plt.ylabel('Demand')
    plt.title(f'Test Observations vs Naive Forecast, {test_size} periods ahead')
    plt.xticks(rotation=45)
    plt.show()
else:
    print('Naive is only possible for one-period ahead forecasts')
    
end_time = time.time()
execution_time = end_time - start_time
print(f"The method took {execution_time} seconds to execute.")

#%%
########################
# Moving Average 
########################
start_time = time.time()

if test_size ==1:
    order_range = np.arange(1, 20, 1)

    rmse_all = []
    orders = []
    forecast_all = []
    test_all = []
    test_indices = []
    
    for fold, (train_index, test_index) in enumerate(tscv.split(data), 1):
        train = []
        validation = []
        test = []
        trainval_data, test_data = data[train_index].tolist(), data[test_index].tolist()
        test.extend(test_data)
        test_indices.extend(test_index)
    
        validation_index = int(len(trainval_data) * percentage) 
        train.extend(trainval_data[:validation_index])
        validation.extend(trainval_data[validation_index:])
    
        train_length = len(train)
        val_length = len(validation)
        test_length = len(test)
        trainval_length = len(trainval_data)
        
        best_rmse = float('inf')
        best_order = None
         
        for order in order_range:
            forecast_val = [] 
            for i in range(val_length):
                if i ==0:
                    total = sum(train[-order:])
                    prediction = total / order
                    forecast_val.append(prediction)
                elif 0< i < order:
                    total = sum(train[-order+i:]) + sum(validation[:i])
                    prediction = total / order
                    forecast_val.append(prediction)
                elif i >= order:
                    total = sum(validation[i-order:i])
                    prediction = total / order
                    forecast_val.append(prediction)
            mse = mean_squared_error(validation, forecast_val)
            rmse = math.sqrt(mse)
            
            if rmse < best_rmse:
                best_rmse = rmse
                best_order = order
        
        orders.append(best_order)
        forecast_test = [] 
        for i in range(test_set_length):
            if i ==0:
                total = sum(trainval_data[-best_order:])
                prediction = total / best_order
                forecast_test.append(prediction)
            elif 0< i < best_order:
                total = sum(trainval_data[-best_order+i:]) + sum(test[:i])
                prediction = total / best_order
                forecast_test.append(prediction)
            elif i >= best_order:
                total = sum(test[i-best_order:i])
                prediction = total / best_order
                forecast_test.append(prediction)
         
    
        forecast_all.extend(forecast_test)
        test_all.extend(test) 
        mse_test = mean_squared_error(test, forecast_test)
        rmse_test = math.sqrt(mse_test)
        rmse_all.append(rmse_test)
                                     
    resulting_rmse = mean(rmse_all)
    forecast_array = np.array(forecast_all)
    test_array = np.array(test_all)

    result = abs(forecast_array - test_array)
    MAE = sum(result) / len(result)
    print("MAE:", MAE)
    
    r_squared = r2_score(test_array, forecast_array)
    print("R-squared:", r_squared)
    
    print("RMSE MA", test_size, "periods ahead forecasting:", resulting_rmse) 

    print("Fold\torder")
    for fold in range(len(orders)):
        print(f"{fold+1}\t{orders[fold]}")
    
    average_order = np.mean(orders)
    print("Average order over all the folds:", average_order)
    
    fig, ax = plt.subplots()
    test_dates = dates[test_indices]  
    ax.plot(test_dates, test_all, label='Test Observations')
    ax.plot(test_dates, forecast_all, label='MA Forecast')
    
    ax.legend()
    plt.xlabel('Date')
    plt.ylabel('Demand')
    plt.title(f'Test Observations vs MA Forecast, {test_size} periods ahead')
    plt.xticks(rotation=45)
    plt.show()
else:
    print('MA is only possible for one-period ahead forecasts')
    
end_time = time.time()
execution_time = end_time - start_time
print(f"The MA method took {execution_time} seconds to execute.")

#%%
########################
# Simple Exponential Smoothing
########################
start_time = time.time()

if test_size == 1:
    
    alpha_range = np.arange(0.01, 1.01, 0.01)
    alphas = []
    rmse_all = []
    forecast_all = []
    test_all = []
    test_indices = [] 
    
    for fold, (train_index, test_index) in enumerate(tscv.split(data), 1):
        train = []
        validation = []
        test = []
        trainval_data, test_data = data[train_index].tolist(), data[test_index].tolist()
        test.extend(test_data)
        test_indices.extend(test_index)

        validation_index = int(len(trainval_data) * percentage) 
        train.extend(trainval_data[:validation_index])
        validation.extend(trainval_data[validation_index:])
            
        train_length = len(train)
        val_length = len(validation)
        test_length = len(test)
        trainval_length = len(trainval_data)
            
        best_rmse = float('inf')
        best_alpha = None
               
        for alpha in alpha_range:
            try:
                forecast_val = []
                if test_size == 1:
                    history = [x for x in train]
                else:
                    history = train[: - test_size +1 ]
                for t in range(0,min(test_size, test_set_length)):
                    model = ExponentialSmoothing(history)
                    model_fit = model.fit(smoothing_level=alpha, optimized=False)
                    yhat = model_fit.forecast(test_size)[-1]
                    forecast_val.append(yhat)
                    if (-(test_size-1)+ t) != 0:
                        obs = train[-(test_size-1)+ t]
                    else:
                        obs = validation[0]
                    history.append(obs)
                for t in range(max(0,val_length-test_size)):
                    model = ExponentialSmoothing(history)
                    model_fit = model.fit(smoothing_level=alpha, optimized=False)
                    yhat = model_fit.forecast(test_size)[-1]
                    forecast_val.append(yhat)
                    obs = validation[t+1]
                    history.append(obs)
                           
                mse = mean_squared_error(validation, forecast_val)
                rmse = math.sqrt(mse)
                   
                if rmse < best_rmse:
                    best_rmse = rmse
                    best_alpha = alpha
            except:
                continue
                
        if best_alpha is None:
            best_alpha = 0.8
        alphas.append(best_alpha)
        
        forecast_test = []
        if test_size == 1:
            history = [x for x in trainval_data]
        else:
            history = trainval_data[: - test_size +1 ]
        for t in range(0,min(test_size, test_set_length)):
            model = ExponentialSmoothing(history)
            model_fit = model.fit(smoothing_level=best_alpha, optimized=False)
            yhat = model_fit.forecast(test_size)[-1]
            forecast_test.append(yhat)
            if (-(test_size-1)+ t) != 0:
                obs = trainval_data[-(test_size-1)+ t]
            else:
                obs = test[0]
            history.append(obs)
        for t in range(max(0,test_set_length-test_size)):
            model = ExponentialSmoothing(history)
            model_fit = model.fit(smoothing_level=best_alpha, optimized=False)
            yhat = model_fit.forecast(test_size)[-1]
            forecast_test.append(yhat)
            obs = test[t+1]
            history.append(obs)    
        
        
        forecast_all.extend(forecast_test)
        test_all.extend(test) 
        mse_test = mean_squared_error(test, forecast_test)
        rmse_test = math.sqrt(mse_test)
        rmse_all.append(rmse_test)    
                                     
    resulting_rmse = mean(rmse_all)
    forecast_array = np.array(forecast_all)
    test_array = np.array(test_all)

    result = abs(forecast_array - test_array)
    MAE = sum(result) / len(result)
    print("MAE:", MAE)
    
    r_squared = r2_score(test_array, forecast_array)
    print("R-squared:", r_squared)

    print("RMSE SES", test_size, "periods ahead forecasting:", resulting_rmse) 

    print("Fold\talpha")
    for fold in range(len(alphas)):
        print(f"{fold+1}\t{alphas[fold]}")
    
    average_alpha = mean(alphas)
    print("Average alpha over all the folds:", average_alpha)
    
    fig, ax = plt.subplots()
    test_dates = dates[test_indices] 
    ax.plot(test_dates, test_all, label='Test Observations')
    ax.plot(test_dates, forecast_all, label='SES Forecast')
    
    ax.legend()
    plt.xlabel('Date')
    plt.ylabel('Demand')
    plt.title(f'Test Observations vs SES, {test_size} periods ahead')
    plt.xticks(rotation=45)
    plt.show()


else:
    print('SES is only possible for one-period ahead forecasts')  

end_time = time.time()
execution_time = end_time - start_time
print(f"The SES method took {execution_time} seconds to execute.")

#%%
########################
# ARIMA
########################
def arima():
    orders = []
    p_range = range(0, 5)
    d_range = range(0, 3) 
    q_range = range(0, 5)
    warnings.filterwarnings("ignore")
    rmse_all = []
    forecast_all = []
    test_all = []
    test_indices = []
    start_time = time.time()

    for fold, (train_index, test_index) in enumerate(tscv.split(data), 1):
        train = []
        validation = []
        test = []
        trainval_data, test_data = data[train_index].tolist(), data[test_index].tolist()
        test.extend(test_data)
        test_indices.extend(test_index)

        validation_index = int(len(trainval_data) * percentage) 
        train.extend(trainval_data[:validation_index])
        validation.extend(trainval_data[validation_index:])
    
        train_length = len(train)
        val_length = len(validation)
        test_length = len(test)
        trainval_length = len(trainval_data)
        
        best_rmse = float('inf')
        best_order = None   

        for p in p_range:
            for d in d_range:
                for q in q_range:
                    order = (p,d,q)
                    try:
                            forecast_val = []
                            if test_size == 1:
                                history = [x for x in train]
                            else:
                                history = train[: - test_size +1 ]
                            for t in range(0,min(test_size, test_set_length)):
                                model = ARIMA(history, order=order)
                                model_fit = model.fit()
                                yhat = model_fit.forecast(test_size)[-1]
                                forecast_val.append(yhat)
                                if (-(test_size-1)+ t) != 0:
                                    obs = train[-(test_size-1)+ t]
                                else:
                                    obs = validation[0]
                                history.append(obs)
                            for t in range(max(0,val_length-test_size)):
                                model = ARIMA(history, order=order)
                                model_fit = model.fit()
                                yhat = model_fit.forecast(test_size)[-1]
                                forecast_val.append(yhat)
                                obs = validation[t+1]
                                history.append(obs)
                                    
                            mse = mean_squared_error(validation, forecast_val)
                            rmse = math.sqrt(mse)
                            if rmse < best_rmse:
                                best_rmse, best_order = rmse, order
                    except: 
                        continue 
        
        if best_order is None:
            best_order = (2,1,2)
        orders.append(best_order)
        
        forecast_test = []
        if test_size == 1:
            history = [x for x in trainval_data]
        else:
            history = trainval_data[: - test_size +1 ]
        for t in range(0,min(test_size, test_set_length)):
            model = ARIMA(history, order=best_order)
            model_fit = model.fit()
            yhat = model_fit.forecast(test_size)[-1]
            forecast_test.append(yhat)
            if (-(test_size-1)+ t) != 0:
                obs = trainval_data[-(test_size-1)+ t]
            else:
                obs = test[0]
            history.append(obs)
        for t in range(max(0,test_set_length-test_size)):
            model = ARIMA(history, order=best_order)
            model_fit = model.fit()
            yhat = model_fit.forecast(test_size)[-1]
            forecast_test.append(yhat)
            obs = test[t+1]
            history.append(obs)        
        
        forecast_all.extend(forecast_test)
        test_all.extend(test) 
        mse_test = mean_squared_error(test, forecast_test)
        rmse_test = math.sqrt(mse_test)
        rmse_all.append(rmse_test)    
                                    
    resulting_rmse = mean(rmse_all)

    for fold in range(len(orders)):
        print(f"{fold+1}\t{orders[fold]}")
        
    p_elements, d_elements, q_elements = zip(*orders)
    average_p = sum(p_elements) / len(p_elements)
    average_d = sum(d_elements) / len(d_elements)
    average_q= sum(q_elements) / len(q_elements)

    print("Average p over all the folds:", average_p, "Integer:", round(average_p))   
    print("Average d over all the folds:", average_d, "Integer:", round(average_d))  
    print("Average q over all the folds:", average_q, "Integer:", round(average_q)) 

    return resulting_rmse, average_p, average_d, average_q 

 

#%%
########################
# HOLT MULTIPLICATIVE
########################

def holt_multiplicative():
    alpha_range = np.arange(0.3, 1.0, 0.05)  
    beta_range = np.arange(0.3, 1.0, 0.05) 
    alphas = []
    betas = []
    rmse_all = []
    forecast_all = []
    test_all = []
    test_indices = [] 
    start_time = time.time()

    for fold, (train_index, test_index) in enumerate(tscv.split(data), 1):
        train = []
        validation = []
        test = []
        trainval_data, test_data = data[train_index].tolist(), data[test_index].tolist()
        test.extend(test_data)
        test_indices.extend(test_index)

        validation_index = int(len(trainval_data) * percentage) 
        train.extend(trainval_data[:validation_index])
        validation.extend(trainval_data[validation_index:])
        
        train_length = len(train)
        val_length = len(validation)
        test_length = len(test)
        trainval_length = len(trainval_data)

        best_rmse = float('inf')
        best_alpha = None
        best_beta = None 
        
        for alpha in alpha_range:
            for beta in beta_range:
                try:
            
                    forecast_val = []
                    if test_size == 1:
                        history = [x for x in train]
                    else:
                        history = train[: - test_size +1 ]
                    for t in range(0,min(test_size, test_set_length)):
                        model = ExponentialSmoothing(history, trend='mul')
                        model_fit = model.fit(smoothing_level=alpha, smoothing_trend=beta, optimized=False)
                        yhat = model_fit.forecast(test_size)[-1]
                        forecast_val.append(yhat)
                        if (-(test_size-1)+ t) != 0:
                            obs = train[-(test_size-1)+ t]
                        else:
                            obs = validation[0]
                        history.append(obs)
                    for t in range(max(0,val_length-test_size)):
                        model = ExponentialSmoothing(history, trend='mul')
                        model_fit = model.fit(smoothing_level=alpha, smoothing_trend=beta, optimized=False)
                        yhat = model_fit.forecast(test_size)[-1]
                        forecast_val.append(yhat)
                        obs = validation[t+1]
                        history.append(obs)
                            
                    mse = mean_squared_error(validation, forecast_val)
                    rmse = math.sqrt(mse)
                    
                    if rmse < best_rmse:
                        best_rmse = rmse
                        best_alpha = alpha
                        best_beta = beta
                except:
                    continue
                
        if best_alpha is None:
            best_alpha = 0.8
                        
        if best_beta is None:
            best_beta = 0.8
        alphas.append(best_alpha)
        betas.append(best_beta)
        #print("Check")

        forecast_test = []
        if test_size == 1:
            history = [x for x in trainval_data]
        else:
            history = trainval_data[: - test_size +1 ]
        for t in range(0,min(test_size, test_set_length)):
            model = ExponentialSmoothing(history, trend='mul')
            model_fit = model.fit(smoothing_level=best_alpha, smoothing_trend=best_beta, optimized=False)
            yhat = model_fit.forecast(test_size)[-1]
            forecast_test.append(yhat)
            if (-(test_size-1)+ t) != 0:
                obs = trainval_data[-(test_size-1)+ t]
            else:
                obs = test[0]
            history.append(obs)
        for t in range(max(0,test_set_length-test_size)):
            model = ExponentialSmoothing(history, trend='mul')
            model_fit = model.fit(smoothing_level=best_alpha, smoothing_trend=best_beta, optimized=False)
            yhat = model_fit.forecast(test_size)[-1]
            forecast_test.append(yhat)
            obs = test[t+1]
            history.append(obs)    
        
        forecast_all.extend(forecast_test)
        test_all.extend(test) 
        mse_test = mean_squared_error(test, forecast_test)
        rmse_test = math.sqrt(mse_test)
        rmse_all.append(rmse_test)    
                                    
    resulting_rmse = mean(rmse_all)
    

    print("Fold\talpha\tbeta")
    for fold in range(len(alphas)):
        print(f"{fold+1}\t{alphas[fold]}\t{betas[fold]}")

    average_alpha = mean(alphas)
    average_beta = mean(betas)
    print("Average alpha over all the folds:", average_alpha)
    print("Average beta over all the folds:", average_beta)

    return resulting_rmse, average_alpha, average_beta


#%%
########################
# DAMPED MULTIPLICATIVE
########################

def damped_holt_multiplicative():
    alpha_range = np.arange(0.3, 1.0, 0.05)
    beta_range = np.arange(0.3, 1.0, 0.05)
    damping_range = np.arange(0.3, 1.0, 0.05)
    alphas = []
    betas = []
    dampings = []
    rmse_all = []
    forecast_all = []
    test_all = []
    test_indices = [] 
    start_time = time.time()

    for fold, (train_index, test_index) in enumerate(tscv.split(data), 1):
        train = []
        validation = []
        test = []
        trainval_data, test_data = data[train_index].tolist(), data[test_index].tolist()
        test.extend(test_data)
        test_indices.extend(test_index)

        validation_index = int(len(trainval_data) * percentage) 
        train.extend(trainval_data[:validation_index])
        validation.extend(trainval_data[validation_index:])
    
        train_length = len(train)
        val_length = len(validation)
        test_length = len(test)
        trainval_length = len(trainval_data)
        
        best_rmse = float('inf')
        best_alpha = None
        best_beta = None
        best_damping = None
            
        for alpha in alpha_range:
            for beta in beta_range:
                for damping in damping_range:
                    try:
                        forecast_val = []
                        if test_size == 1:
                            history = [x for x in train]
                        else:
                            history = train[: - test_size +1 ]
                        for t in range(0,min(test_size, test_set_length)):
                            model = ExponentialSmoothing(history, trend='mul', damped_trend = True)
                            model_fit = model.fit(smoothing_level=alpha, smoothing_trend=beta, damping_trend=damping, optimized=False)
                            yhat = model_fit.forecast(test_size)[-1]
                            forecast_val.append(yhat)
                            if (-(test_size-1)+ t) != 0:
                                obs = train[-(test_size-1)+ t]
                            else:
                                obs = validation[0]
                            history.append(obs)
                        for t in range(max(0,val_length-test_size)):
                            model = ExponentialSmoothing(history, trend='mul', damped_trend = True)
                            model_fit = model.fit(smoothing_level=alpha, smoothing_trend=beta, damping_trend=damping, optimized=False)
                            yhat = model_fit.forecast(test_size)[-1]
                            forecast_val.append(yhat)
                            obs = validation[t+1]
                            history.append(obs)
                                
                        mse = mean_squared_error(validation, forecast_val)
                        rmse = math.sqrt(mse)
                        
                        if rmse < best_rmse:
                            best_rmse = rmse
                            best_alpha = alpha
                            best_beta = beta
                            best_damping = damping
                    except:
                        continue
                
        if best_alpha is None:
            best_alpha = 0.8
        if best_beta is None:
            best_beta = 0.8
        if best_damping is None:
            best_damping = 0.8
        alphas.append(best_alpha)
        betas.append(best_beta)
        dampings.append(best_damping)   

        forecast_test = []
        if test_size == 1:
            history = [x for x in trainval_data]
        else:
            history = trainval_data[: - test_size +1 ]
        for t in range(0,min(test_size, test_set_length)):
            model = ExponentialSmoothing(history, trend='mul', damped_trend = True)
            model_fit = model.fit(smoothing_level=best_alpha, smoothing_trend=best_beta, damping_trend=best_damping, optimized=False)
            yhat = model_fit.forecast(test_size)[-1]
            forecast_test.append(yhat)
            if (-(test_size-1)+ t) != 0:
                obs = trainval_data[-(test_size-1)+ t]
            else:
                obs = test[0]
            history.append(obs)
        for t in range(max(0,test_set_length-test_size)):
            model = ExponentialSmoothing(history, trend='mul', damped_trend = True)
            model_fit = model.fit(smoothing_level=best_alpha, smoothing_trend=best_beta, damping_trend=best_damping, optimized=False)
            yhat = model_fit.forecast(test_size)[-1]
            forecast_test.append(yhat)
            obs = test[t+1]
            history.append(obs)       
        
        forecast_all.extend(forecast_test)
        test_all.extend(test) 
        mse_test = mean_squared_error(test, forecast_test)
        rmse_test = math.sqrt(mse_test)
        rmse_all.append(rmse_test)    
                                    
    resulting_rmse = mean(rmse_all) 

    print("Fold\talpha\tbeta\tdamping")
    for fold in range(len(alphas)):
        print(f"{fold+1}\t{alphas[fold]}\t{betas[fold]}\t{dampings[fold]}")

    average_alpha = mean(alphas)
    average_beta = mean(betas)
    average_damping = mean(dampings)
    print("Average alpha over all the folds:", average_alpha)
    print("Average beta over all the folds:", average_beta)
    print("Average damping over all the folds:", average_damping)

    return resulting_rmse, average_alpha, average_beta, average_damping


#%%
########################
# HOLT WINTER 
########################

def holt_winter():
    alpha_range = np.arange(0.3, 1.0, 0.05)
    beta_range = np.arange(0.3, 1.0, 0.05)
    gamma_range = np.arange(0.3, 1.0, 0.05)

    alphas = []
    betas = []
    gammas = []
    rmse_all = []
    forecast_all = []
    test_all = []
    test_indices = [] 
    start_time = time.time()

    for fold, (train_index, test_index) in enumerate(tscv.split(data), 1):
        train = []
        validation = []
        test = []
        trainval_data, test_data = data[train_index].tolist(), data[test_index].tolist()
        test.extend(test_data)
        test_indices.extend(test_index)

        validation_index = int(len(trainval_data) * percentage) 
        train.extend(trainval_data[:validation_index])
        validation.extend(trainval_data[validation_index:])

        train_length = len(train)
        val_length = len(validation)
        test_length = len(test)
        trainval_length = len(trainval_data)

        best_rmse = float('inf')
        best_alpha = None
        best_beta = None
        best_gamma = None   
        
        for alpha in alpha_range:
            for beta in beta_range:
                for gamma in gamma_range:
                    try:
                        forecast_val = []
                        if test_size == 1:
                            history = [x for x in train]
                        else:
                            history = train[: - test_size +1 ]
                        for t in range(0,min(test_size, test_set_length)):
                            model = ExponentialSmoothing(history, seasonal_periods=4, trend='mul', seasonal='mul')
                            model_fit = model.fit(smoothing_level=alpha, smoothing_trend=beta, smoothing_seasonal=gamma, optimized=False)
                            yhat = model_fit.forecast(test_size)[-1]
                            forecast_val.append(yhat)
                            if (-(test_size-1)+ t) != 0:
                                obs = train[-(test_size-1)+ t]
                            else:
                                obs = validation[0]
                            history.append(obs)
                        for t in range(max(0,val_length-test_size)):
                            model = ExponentialSmoothing(history, seasonal_periods=4, trend='mul', seasonal='mul')
                            model_fit = model.fit(smoothing_level=alpha, smoothing_trend=beta, smoothing_seasonal=gamma, optimized=False)
                            yhat = model_fit.forecast(test_size)[-1]
                            forecast_val.append(yhat)
                            obs = validation[t+1]
                            history.append(obs)
                                
                        mse = mean_squared_error(validation, forecast_val)
                        rmse = math.sqrt(mse)
                        
                        if rmse < best_rmse:
                            best_rmse = rmse
                            best_alpha = alpha
                            best_beta = beta
                            best_gamma = gamma
                    except:
                        continue
                
        if best_alpha is None:
            best_alpha = 0.8
        if best_beta is None:
            best_beta = 0.8
        if best_gamma is None:
            best_gamma = 0.8
        alphas.append(best_alpha)
        betas.append(best_beta)
        gammas.append(best_gamma)
        print("Check")    

        forecast_test = []
        if test_size == 1:
            history = [x for x in trainval_data]
        else:
            history = trainval_data[: - test_size +1 ]
        for t in range(0,min(test_size, test_set_length)):
            model = ExponentialSmoothing(history, seasonal_periods=4, trend='mul', seasonal='mul')
            model_fit = model.fit(smoothing_level=best_alpha, smoothing_trend=best_beta, smoothing_seasonal=best_gamma, optimized=False)
            yhat = model_fit.forecast(test_size)[-1]
            forecast_test.append(yhat)
            if (-(test_size-1)+ t) != 0:
                obs = trainval_data[-(test_size-1)+ t]
            else:
                obs = test[0]
            history.append(obs)
        for t in range(max(0,test_set_length-test_size)):
            model = ExponentialSmoothing(history, seasonal_periods=4, trend='mul', seasonal='mul')
            model_fit = model.fit(smoothing_level=best_alpha, smoothing_trend=best_beta, smoothing_seasonal=best_gamma, optimized=False)
            yhat = model_fit.forecast(test_size)[-1]
            forecast_test.append(yhat)
            obs = test[t+1]
            history.append(obs)    
        
        
        forecast_all.extend(forecast_test)
        test_all.extend(test) 
        mse_test = mean_squared_error(test, forecast_test)
        rmse_test = math.sqrt(mse_test)
        rmse_all.append(rmse_test)    
                                    
    resulting_rmse = mean(rmse_all)

    print("Fold\talpha\tbeta\tgamma")
    for fold in range(len(alphas)):
        print(f"{fold+1}\t{alphas[fold]}\t{betas[fold]}\t{gammas[fold]}")

    average_alpha = mean(alphas)
    average_beta = mean(betas)
    average_gamma = mean(gammas)
    print("Average alpha over all the folds:", average_alpha)
    print("Average beta over all the folds:", average_beta)
    print("Average gamma over all the folds:", average_gamma)

    return resulting_rmse, average_alpha, average_beta, average_gamma

#%%
########################
# HOLT WINTER DAMPED 
########################

def holt_winter_damped():
    alpha_range = np.arange(0.3, 1.0, 0.1)
    beta_range = np.arange(0.3, 1.0, 0.1)
    gamma_range = np.arange(0.3, 1.0, 0.1)
    damping_range = np.arange(0.3, 1.0, 0.1)
    alphas = []
    betas = []
    gammas = []
    dampings = []
    rmse_all = []
    forecast_all = []
    test_all = []
    test_indices = [] 
    start_time = time.time()

    for fold, (train_index, test_index) in enumerate(tscv.split(data), 1):
        train = []
        validation = []
        test = []
        trainval_data, test_data = data[train_index].tolist(), data[test_index].tolist()
        test.extend(test_data)
        test_indices.extend(test_index)

        validation_index = int(len(trainval_data) * percentage) 
        train.extend(trainval_data[:validation_index])
        validation.extend(trainval_data[validation_index:])
    
        train_length = len(train)
        val_length = len(validation)
        test_length = len(test)
        trainval_length = len(trainval_data)
        
        best_rmse = float('inf')
        best_alpha = None
        best_beta = None
        best_gamma = None
        best_damping = None    
        
        for alpha in alpha_range:
            for beta in beta_range:
                for gamma in gamma_range:
                    for damping in damping_range:
                        try:
                            forecast_val = []
                            if test_size == 1:
                                history = [x for x in train]
                            else:
                                history = train[: - test_size +1 ]
                            for t in range(0,min(test_size, test_set_length)):
                                model = ExponentialSmoothing(history, seasonal_periods=4, trend='mul', seasonal='mul', damped_trend = True)
                                model_fit = model.fit(smoothing_level=alpha, smoothing_trend=beta, smoothing_seasonal=gamma, damping_trend=damping, optimized=False)
                                yhat = model_fit.forecast(test_size)[-1]
                                forecast_val.append(yhat)
                                if (-(test_size-1)+ t) != 0:
                                    obs = train[-(test_size-1)+ t]
                                else:
                                    obs = validation[0]
                                history.append(obs)
                            for t in range(max(0,val_length-test_size)):
                                model = ExponentialSmoothing(history, seasonal_periods=4, trend='mul', seasonal='mul', damped_trend = True)
                                model_fit = model.fit(smoothing_level=alpha, smoothing_trend=beta, smoothing_seasonal=gamma, damping_trend=damping, optimized=False)
                                yhat = model_fit.forecast(test_size)[-1]
                                forecast_val.append(yhat)
                                obs = validation[t+1]
                                history.append(obs)
                                    
                            mse = mean_squared_error(validation, forecast_val)
                            rmse = math.sqrt(mse)
                            
                            if rmse < best_rmse:
                                best_rmse = rmse
                                best_alpha = alpha
                                best_beta = beta
                                best_gamma = gamma
                                best_damping = damping
                        except:
                            continue
                
        if best_alpha is None:
            best_alpha = 0.8
        if best_beta is None:
            best_beta = 0.8
        if best_gamma is None:
            best_gamma = 0.8
        alphas.append(best_alpha)
        betas.append(best_beta)
        gammas.append(best_gamma)
        dampings.append(best_damping)
        print("Check")   

        forecast_test = []
        if test_size == 1:
            history = [x for x in trainval_data]
        else:
            history = trainval_data[: - test_size +1 ]
        for t in range(0,min(test_size, test_set_length)):
            model = ExponentialSmoothing(history, seasonal_periods=4, trend='mul', seasonal='mul', damped_trend=True)
            model_fit = model.fit(smoothing_level=best_alpha, smoothing_trend=best_beta, smoothing_seasonal=best_gamma, damping_trend=best_damping, optimized=False)
            yhat = model_fit.forecast(test_size)[-1]
            forecast_test.append(yhat)
            if (-(test_size-1)+ t) != 0:
                obs = trainval_data[-(test_size-1)+ t]
            else:
                obs = test[0]
            history.append(obs)
        for t in range(max(0,test_set_length-test_size)):
            model = ExponentialSmoothing(history, seasonal_periods=4, trend='mul', seasonal='mul', damped_trend=True)
            model_fit = model.fit(smoothing_level=best_alpha, smoothing_trend=best_beta, smoothing_seasonal=best_gamma, damping_trend=best_damping, optimized=False)
            yhat = model_fit.forecast(test_size)[-1]
            forecast_test.append(yhat)
            obs = test[t+1]
            history.append(obs)    
        
        forecast_all.extend(forecast_test)
        test_all.extend(test) 
        mse_test = mean_squared_error(test, forecast_test)
        rmse_test = math.sqrt(mse_test)
        rmse_all.append(rmse_test)    
                                    
    resulting_rmse = mean(rmse_all)


    print("Fold\talpha\tbeta\tgamma\tdamping")
    for fold in range(len(alphas)):
        print(f"{fold+1}\t{alphas[fold]}\t{betas[fold]}\t{gammas[fold]}\t{dampings[fold]}")

    average_alpha = mean(alphas)
    average_beta = mean(betas)
    average_gamma = mean(gammas)
    average_damping = mean(dampings)
    print("Average alpha over all the folds:", average_alpha)
    print("Average beta over all the folds:", average_beta)
    print("Average gamma over all the folds:", average_gamma)
    print("Average damping over all the folds:", average_damping)

    return resulting_rmse, average_alpha, average_beta, average_gamma, average_damping


#%%
########################
# SARIMA
########################

def sarima():
    orders = []
    seasonal_orders = []
    p_range = [1,2]
    d_range = [1]
    q_range = [1,2]
    P_range = [1,2]
    D_range = [1]
    Q_range = [1,2]
    m_range = [4]
    warnings.filterwarnings("ignore")
    rmse_all = []
    forecast_all = []
    test_all = []
    test_indices = []
    start_time = time.time()

    for fold, (train_index, test_index) in enumerate(tscv.split(data), 1):
        train = []
        validation = []
        test = []
        trainval_data, test_data = data[train_index].tolist(), data[test_index].tolist()
        test.extend(test_data)
        test_indices.extend(test_index)

        validation_index = int(len(trainval_data) * percentage) 
        train.extend(trainval_data[:validation_index])
        validation.extend(trainval_data[validation_index:])

        train_length = len(train)
        val_length = len(validation)
        test_length = len(test)
        trainval_length = len(trainval_data)

        best_rmse = float('inf')
        best_order = None
        best_seasonal = None

        for p in p_range:
                for d in d_range:
                    for q in q_range:
                        for P in P_range:
                            for D in D_range:
                                for Q in Q_range:
                                    for m in m_range:
                                        order = (p,d,q)
                                        seasonal_order = (P,D,Q,m)
                                        try:
                                            forecast_val = []
                                            if test_size == 1:
                                                history = [x for x in train]
                                            else:
                                                history = train[: - test_size +1 ]
                                            for t in range(0,min(test_size, test_set_length)):
                                                model = SARIMAX(history, order=order, seasonal_order=seasonal_order)
                                                model_fit = model.fit(disp=False)
                                                yhat = model_fit.forecast(test_size)[-1]
                                                forecast_val.append(yhat)
                                                if (-(test_size-1)+ t) != 0:
                                                    obs = train[-(test_size-1)+ t]
                                                else:
                                                    obs = validation[0]
                                                history.append(obs)
                                            for t in range(max(0,val_length-test_size)):
                                                model = SARIMAX(history, order=order, seasonal_order=seasonal_order)
                                                model_fit = model.fit(disp=False)
                                                yhat = model_fit.forecast(test_size)[-1]
                                                forecast_val.append(yhat)
                                                obs = validation[t+1]
                                                history.append(obs)
                                                    
                                            mse = mean_squared_error(validation, forecast_val)
                                            rmse = math.sqrt(mse)
                                        
                                            if rmse < best_rmse:
                                                best_rmse, best_order, best_seasonal = rmse, order, seasonal_order
                                        except: 
                                            continue 
        
        if best_order is None:
            best_order = (2,1,2)
        if best_seasonal is None:
            best_seasonal = (2,1,2,52)
        
        orders.append(best_order)
        seasonal_orders.append(best_seasonal)
        print("Check")

        forecast_test = []
        if test_size == 1:
            history = [x for x in trainval_data]
        else:
            history = trainval_data[: - test_size +1 ]
        for t in range(0,min(test_size, test_set_length)):
            model = SARIMAX(history, order=best_order, seasonal_order=best_seasonal)
            model_fit = model.fit(disp=False)
            yhat = model_fit.forecast(test_size)[-1]
            forecast_test.append(yhat)
            if (-(test_size-1)+ t) != 0:
                obs = trainval_data[-(test_size-1)+ t]
            else:
                obs = test[0]
            history.append(obs)
        for t in range(max(0,test_set_length-test_size)):
            model = SARIMAX(history, order=best_order, seasonal_order=best_seasonal)
            model_fit = model.fit(disp=False)
            yhat = model_fit.forecast(test_size)[-1]
            forecast_test.append(yhat)
            obs = test[t+1]
            history.append(obs)    
        
        forecast_all.extend(forecast_test)
        test_all.extend(test) 
        mse_test = mean_squared_error(test, forecast_test)
        rmse_test = math.sqrt(mse_test)
        rmse_all.append(rmse_test)    
                                    
    resulting_rmse = mean(rmse_all)

    print("Fold\torder\tseasonal order")
    for fold in range(len(orders)):
        print(f"{fold+1}\t{orders[fold]}\t{seasonal_orders[fold]}")
        
    p_elements, d_elements, q_elements = zip(*orders)
    average_p = sum(p_elements) / len(p_elements)
    average_d = sum(d_elements) / len(d_elements)
    average_q= sum(q_elements) / len(q_elements)
    print("Average p over all the folds:", average_p, "Integer:", round(average_p))   
    print("Average d over all the folds:", average_d, "Integer:", round(average_d))  
    print("Average q over all the folds:", average_q, "Integer:", round(average_q))  

    P_elements, D_elements, Q_elements, m_elements = zip(*seasonal_orders)
    average_P = sum(P_elements) / len(P_elements)
    average_D = sum(D_elements) / len(D_elements)
    average_Q= sum(Q_elements) / len(Q_elements)
    average_m= sum(m_elements) / len(m_elements)
    print("Average P over all the folds:", average_P, "Integer:", round(average_P))   
    print("Average D over all the folds:", average_D, "Integer:", round(average_D))  
    print("Average Q over all the folds:", average_Q, "Integer:", round(average_Q))  
    print("Average m over all the folds:", average_m, "Integer:", round(average_m)) 

    return resulting_rmse, average_p, average_d, average_q, average_P, average_D, average_Q, average_m 

 #%%
