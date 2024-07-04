## group 17
# Anne Rutgers
# Dico de Gier
# Daan Spanbroek
# Nick Verkaik

import numpy as np
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt
np.random.seed(1)

# we used this code to find our definitions_group17 file
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from definitions_group17 import *

## QUESTION 1A
print("-----------question 1A:-----------")

# Read the CSV file containing historical data
data = pd.read_csv('AEX_group17.csv')
prices = data['Close']
S_0 = prices[0]

# Calculate daily returns
log_returns = np.log(prices / prices.shift(1)).dropna()

# Calculate mean and standard deviation of log returns
mu = log_returns.mean()
sigma = log_returns.std()

print(f"S_0: {S_0}")
print(f"mu: {mu}")
print(f"sigma: {sigma}")


## QUESTION 1B
print("-----------question 1B:-----------")

S_0 = 787.02                # initial price risky asset (exercise 1a)
K = 740                     # option strike price
r = -0.00567                # assumed risk-free interest rate
T = 5                       # time to maturity
sigma = 0.1790              # annual volatility (exercise 1a)
confidence_level = 0.95     # for a 95% confidence interval

num_simulations = 10000
option_prices = []

for _ in range(num_simulations):
    stock = np.zeros(T + 1)
    stock[0] = S_0
    for time in range(1, T + 1): 
        stock[time] = stock[time-1] * np.exp((r - 0.5 * sigma**2) + sigma * np.random.normal(0,1))
    payoff = max(0, K - (1/T) * np.sum(stock))
    option_prices.append(payoff * np.exp(-r * T))

mean_price = np.mean(option_prices)
std_dev = np.std(option_prices)  
z_score = norm.ppf((1 + confidence_level) / 2)

lower_bound = mean_price - z_score * (std_dev / np.sqrt(num_simulations))
upper_bound = mean_price + z_score * (std_dev / np.sqrt(num_simulations))

print(f"95% Confidence Interval: ({lower_bound:.4f}, {upper_bound:.4f})")

## QUESTION 1C
print("-----------question 1C:-----------")

S_0 = 787.02            # initial value risky asset
T = 5                   # time to maturity
sigma = 0.1790          # annual volatility
r = -0.00567            # interest rate
K = 740                 # strike price

# bump and reprice using common numbers

n = 10000               # number of simulations
h = 0.0001              # bump

put_delta_bump_reprice_mean, put_delta_bump_reprice_LB, put_delta_bump_reprice_UB = approximate_delta_put_bump_reprice_common_CI_delta(n, S_0, T, sigma, r, K, h)

print(f"95% Confidence Interval Delta (common numbers): ({put_delta_bump_reprice_LB:.4f}, {put_delta_bump_reprice_UB:.4f})")
print(f"Mean Delta (common numbers): {put_delta_bump_reprice_mean:.4f}")

# bump and reprice using independent numbers

n = 10000               # number of simulations
h = n**(-1/4)           # bump

put_delta_bump_reprice_mean_indep, put_delta_bump_reprice_LB_indep, put_delta_bump_reprice_UB_indep = approximate_delta_put_bump_reprice_noncommon_CI_delta(n, S_0, T, sigma, r, K, h)

print(f"95% Confidence Interval Delta (independent numbers): ({put_delta_bump_reprice_LB_indep:.4f}, {put_delta_bump_reprice_UB_indep:.4f})")
print(f"Mean Delta (independent numbers): {put_delta_bump_reprice_mean_indep:.4f}")


## QUESTION 2A
print("-----------question 2A:-----------")

mu = 0.1            # drift
sigma = 0.25        # volatility
S_0 = 100           # initial price risky asset
B_0 = 1             # initial price riskless bond
r = 0.03            # interest rate 
K = 100             # strike price
T = 2               # time to maturity 

n = 10000           # number of simulations
h = 0.0001          # choose small

put = BlackScholesOptionPrice(K, r, sigma)

# exact calculation of delta
delta = put.delta_put(current_stock_price=S_0, time_to_maturity=T)
print(f"Exact calculation of delta gives: delta = {delta:.4f}")

# bump-and-reprice method delta
put_delta_bump_reprice = approximate_delta_put_bump_reprice_common(n, S_0, T, sigma, r, K, h)
print(f"Calculation of delta using bump-and-reprice gives: delta {put_delta_bump_reprice:.4f}")

# pathwise method delta
put_delta_pathwise = approximate_delta_put_pathwise_common(n, S_0, T, sigma, r, K)
print(f"Calculation of delta using the pathwise method gives: delta {put_delta_pathwise:.4f}")

# likelihood ratio method delta
put_delta_likelihood_ratio = approximate_delta_put_likelihood_ratio_common(n, S_0, T, sigma, r, K)
print(f"Calculation of delta using the likelihood ratio method gives: delta {put_delta_likelihood_ratio:.4f}")


## QUESTION 2B
print("-----------question 2B:-----------")

# exact calculation of gamma
gamma = put.gamma_put(current_stock_price=S_0, time_to_maturity=T)
print(f"Exact calculation of gamma gives: gamma = {gamma:.4f}")

# bump-and-reprice method gamma
put_gamma_bump_reprice = approximate_gamma_put_bump_and_reprice_common(n, S_0, T, sigma, r, K, h)
print(f"Calculation of gamma using bump-and-reprice gives: gamma {put_gamma_bump_reprice:.4f}")

# pathwise method gamma 
# not possible because of the first derivative not being continuous
print("Calculation of delta using the pathwise method: not possible")

# likelihood ratio method gamma
put_gamma_likelihood_ratio = approximate_gamma_put_likelihood_ratio_common(n, S_0, T, sigma, r, K)
print(f"Calculation of gamma using the likelihood ratio method gives: gamma {put_gamma_likelihood_ratio:.4f}")


## QUESTION 2C
print("-----------question 2C:-----------")

# stepsize:
time_delta = 0.01
# parameters GBM for S:
S_0 = 100
mu = 0.10
sigma = 0.25
# parameters B:
B_0 = 1
r = 0.03
# put option:
T = 2
K = 100
num_puts = -1000 
# number of simulations
M=2500

# the following function was taken from the notebook
def writing_put_option_delta_hedge_discrete_time(K: float, T: float, S_0: float, mu: float, sigma: float,
                                                 B_0: float, r: float,
                                                num_puts: int
                                                 ):
    num_time_steps_total = int(T / time_delta)
    # initialize variables:
    phi = np.zeros(num_time_steps_total + 1)
    psi = np.zeros(num_time_steps_total + 1)
    phi[-1] = np.nan
    psi[-1] = np.nan
    price_puts = np.zeros(num_time_steps_total + 1)
    S = np.zeros(num_time_steps_total + 1)
    S[0] = S_0
    B = np.zeros(num_time_steps_total + 1)
    B[0] = B_0
    total_portfolio_value = np.zeros(num_time_steps_total + 1)
    put = BlackScholesOptionPrice(K, r, sigma)
    time = np.linspace(0, T, num_time_steps_total + 1)
    # determine initial positions:
    put_price_initial = put.price_put(current_stock_price=S_0, time_to_maturity=T)
    price_puts[0] = num_puts * put_price_initial
    phi[0] = - num_puts * put.delta_put(current_stock_price=S_0, time_to_maturity=T) # make total portfolio delta-neutral
    psi[0] = - (price_puts[0] + phi[0] * S[0]) / B[0]
    total_portfolio_value[0] = price_puts[0] + phi[0] * S[0] + psi[0] * B[0] # 0 by construction
    # iterate over discrete-time grid:
    for k in range(1, num_time_steps_total + 1):
        # new asset prices:
        B[k] = B[k - 1] * np.exp(r * time_delta)
        S[k] = S[k - 1] * np.exp((mu - 0.5 * sigma ** 2) * time_delta + sigma * np.sqrt(time_delta) * norm.rvs())
        # current value of (S,B) portfolio from previous point-in-time (below we will rebalance):
        value = phi[k - 1] * S[k] + psi[k - 1] * B[k]
        # new value puts:
        if time[k] == T:
            price_puts[k] =  num_puts * np.maximum(K - S[k], 0)
            total_portfolio_value[k] = price_puts[k] + value
            break 
        price_puts[k] = num_puts * put.price_put(current_stock_price=S[k], time_to_maturity=T - time[k])
        # determine new position S for next interval (such that combination of (S, B)-portfolio and 
        # puts is delta-neutral):
        phi[k] =  - num_puts * put.delta_put(current_stock_price=S[k], time_to_maturity=T - time[k])
        # determine new position B, such that there is no net cashflow in (S, B)-portfolio:
        psi[k] = (value - phi[k] * S[k]) / B[k]
        # mismatch between discrete-time delta-neutral, self-financing portfolio and price puts:
        total_portfolio_value[k] = price_puts[k] + phi[k] * S[k] + psi[k] * B[k]
    return time, S, B, phi, psi, price_puts, total_portfolio_value

time, S, B, phi, psi, price_puts, total_portfolio_value = writing_put_option_delta_hedge_discrete_time(K, T, S_0, mu, sigma,B_0, r, num_puts)
print("initial position in stock:" + str(phi[0]))
print("initial position in money market account:" + str(psi[0]))

# create arrays to store results from simulations
sims_S = np.zeros((1,int(T/time_delta)+1))
sims_B = np.zeros((1,int(T/time_delta)+1))
sims_phi = np.zeros((1,int(T/time_delta)+1))
sims_psi = np.zeros((1,int(T/time_delta)+1))
sims_price_puts = np.zeros((1,int(T/time_delta)+1))
sims_total_portfolio_value = np.zeros((1,int(T/time_delta)+1))
sims_gamma = np.zeros((1,int(T/time_delta)+1))

put = BlackScholesOptionPrice(K, r, sigma)
all_gammas = np.zeros((1,int(T/time_delta)+1))

for sim in range(M):
    print("Simulation:" + str(sim), end = '\r')
    time, S, B, phi, psi, price_puts, total_portfolio_value = writing_put_option_delta_hedge_discrete_time(K, T, S_0, mu, sigma,
                                                              B_0, r, num_puts)
    gammas = np.array([])
    
    # calculate gamma at each point in time
    for i in range(len(S)):
        current_stock_price = S[i]
        current_time = time[i]
        current_time_to_maturity = T - current_time
        gamma = put.gamma_put(current_stock_price, current_time_to_maturity)
        gammas = np.append(gammas, gamma)

    # append gamma    
    gammas = gammas.reshape(1,-1)    
    all_gammas = np.r_[all_gammas,gammas]

    # append all other results    
    S = S.reshape(1,-1)
    sims_S = np.r_[sims_S, S]
    B = B.reshape(1,-1)
    sims_B = np.r_[sims_B, B]
    phi = phi.reshape(1,-1)
    sims_phi = np.r_[sims_phi, phi]
    psi = psi.reshape(1,-1)
    sims_psi = np.r_[sims_psi, psi]
    price_puts = price_puts.reshape(1,-1)
    sims_price_puts = np.r_[sims_price_puts, price_puts]
    total_portfolio_value = total_portfolio_value.reshape(1,-1)
    sims_total_portfolio_value = np.r_[sims_total_portfolio_value, total_portfolio_value]

# remove first row of zeros
sims_S = sims_S[1:]
sims_B = sims_B[1:]
sims_phi = sims_phi[1:]
sims_psi = sims_psi[1:]
sims_price_puts = sims_price_puts[1:]
sims_total_portfolio_value = sims_total_portfolio_value[1:]
all_gammas = all_gammas[1:]
 
# preallocate arrays for quantiles
percentiles_phi_5 = np.zeros((int(T/time_delta)+1))
percentiles_phi_50 = np.zeros((int(T/time_delta)+1)) 
percentiles_phi_95 = np.zeros((int(T/time_delta)+1))

percentiles_psi_5 = np.zeros((int(T/time_delta)+1))
percentiles_psi_50 = np.zeros((int(T/time_delta)+1)) 
percentiles_psi_95 = np.zeros((int(T/time_delta)+1))

percentiles_gamma_5 = np.zeros((int(T/time_delta)+1))
percentiles_gamma_50 = np.zeros((int(T/time_delta)+1)) 
percentiles_gamma_95 = np.zeros((int(T/time_delta)+1))

# calculate quantiles by taking simulated data for every point in time
for j in range(int(T/time_delta)+1):
    perc5 = np.percentile(sims_phi[:,j], 5)
    perc50 = np.percentile(sims_phi[:,j], 50)
    perc95 = np.percentile(sims_phi[:,j], 95)
    
    percentiles_phi_5[j] = perc5
    percentiles_phi_50[j] = perc50
    percentiles_phi_95[j] = perc95

    perc5 = np.percentile(sims_psi[:,j], 5)
    perc50 = np.percentile(sims_psi[:,j], 50)
    perc95 = np.percentile(sims_psi[:,j], 95)
    
    percentiles_psi_5[j] = perc5
    percentiles_psi_50[j] = perc50
    percentiles_psi_95[j] = perc95

    perc5 = np.percentile(all_gammas[:,j], 5)
    perc50 = np.percentile(all_gammas[:,j], 50)
    perc95 = np.percentile(all_gammas[:,j], 95)
    
    percentiles_gamma_5[j] = perc5
    percentiles_gamma_50[j] = perc50
    percentiles_gamma_95[j] = perc95

# plot the results
x = np.arange(0,int(T/time_delta)+1)
plt.xlabel("Time")
plt.ylabel("Percentile Values")
plt.title("Simulations of psi")
plt.plot(x,percentiles_psi_5, label = '5th quantile psi')
plt.plot(x,percentiles_psi_50, label = '50th quantile psi')
plt.plot(x,percentiles_psi_95, label = '95th quantile psi')
plt.legend(loc = "upper right")
plt.show()

plt.xlabel("Time")
plt.ylabel("Percentile Values")
plt.title("Simulations of phi")
plt.plot(x,percentiles_phi_5, label = '5th quantile phi')
plt.plot(x,percentiles_phi_50, label = '50th quantile phi')
plt.plot(x,percentiles_phi_95, label = '95th quantile phi')
plt.legend(loc = "upper right")
plt.show()

plt.xlabel("Time")
plt.ylabel("Percentile Values")
plt.title("Simulations of gamma")
plt.plot(x,percentiles_gamma_5, label = '5th quantile gamma')
plt.plot(x,percentiles_gamma_50, label = '50th quantile gamma')
plt.plot(x,percentiles_gamma_95, label = '95th quantile gamma')
plt.legend(loc = "upper right")
plt.show()

mean_total_portfolio_value_maturity = np.mean(sims_total_portfolio_value[:,-1])
print(f"mean of the total portfolio value at maturity {mean_total_portfolio_value_maturity:.4f} ")
std_total_portfolio_value_maturity = np.std(sims_total_portfolio_value[:,-1])
print(f"standard deviation of the total portfolio value at maturity {std_total_portfolio_value_maturity:.4f} ")
price_put = put.price_put(S_0, T)
print("price of the put is " + str(price_put))
print("price of 1000 puts is " + str(price_put*num_puts))

## QUESTION 2Di
print("-----------question 2Di:-----------")

# stepsize:
time_delta = 0.01
# parameters GBM for S:
S_0 = 100
mu = 0.10
sigma = 0.25
# parameters B:
B_0 = 1
r = 0.03

# put option
T = 2
K = 100

# call option  
T_call = 5
K_call = 120

# number of simulations
M=2500

num_puts = -1000 

# this function is the previous function but now adjusted for delta-gamma hedging
def writing_put_option_delta_gamma_hedge_discrete_time(K: float, T: float, S_0: float, mu: float, sigma: float,
                                                 B_0: float, r: float,
                                                num_puts: int
                                                 ):
    num_time_steps_total = int(T / time_delta)
    # initialize variables:
    phi = np.zeros(num_time_steps_total + 1)
    psi = np.zeros(num_time_steps_total + 1)
    calls = np.zeros(num_time_steps_total + 1)
    phi[-1] = np.nan
    psi[-1] = np.nan
    calls[-1] = np.nan
    price_puts = np.zeros(num_time_steps_total + 1)
    S = np.zeros(num_time_steps_total + 1)
    S[0] = S_0
    B = np.zeros(num_time_steps_total + 1)
    B[0] = B_0
    total_portfolio_value = np.zeros(num_time_steps_total + 1)
    put = BlackScholesOptionPrice(K, r, sigma)
    call = BlackScholesOptionPrice(K_call, r, sigma)
    time = np.linspace(0, T, num_time_steps_total + 1)
    # determine initial positions:
    put_price_initial = put.price_put(current_stock_price=S_0, time_to_maturity=T)
    price_puts[0] = num_puts * put_price_initial
    phi[0] = - num_puts * put.delta_put(current_stock_price=S_0, time_to_maturity=T) # make total portfolio delta-neutral

    # buy calls to compensate for the gamma, then change phi i.o.t. compensate for the extra delta
    gamma_put = put.gamma_put(current_stock_price=S_0, time_to_maturity=T)
    gamma_portfolio = num_puts * gamma_put
    gamma_call = call.gamma_call(current_stock_price=S_0, time_to_maturity=T_call)
    calls[0] = - gamma_portfolio/gamma_call
    delta_call = call.delta_call(current_stock_price=S_0, time_to_maturity=T_call)
    extra_delta = calls[0] * delta_call
    phi[0] = phi[0] - extra_delta

    psi[0] = - (price_puts[0] + phi[0] * S[0]) / B[0]
    total_portfolio_value[0] = price_puts[0] + phi[0] * S[0] + psi[0] * B[0] # 0 by construction
    # iterate over discrete-time grid:
    for k in range(1, num_time_steps_total + 1):
        # new asset prices:
        B[k] = B[k - 1] * np.exp(r * time_delta)
        S[k] = S[k - 1] * np.exp((mu - 0.5 * sigma ** 2) * time_delta + sigma * np.sqrt(time_delta) * norm.rvs())
        # current value of (S,B) portfolio from previous point-in-time (below we will rebalance):
        value = phi[k - 1] * S[k] + psi[k - 1] * B[k]
        # new value puts:
        if time[k] == T:
            price_puts[k] =  num_puts * np.maximum(K - S[k], 0)
            total_portfolio_value[k] = price_puts[k] + value
            break 
        price_puts[k] = num_puts * put.price_put(current_stock_price=S[k], time_to_maturity=T - time[k])
        # determine new position S for next interval (such that combination of (S, B)-portfolio and 
        # puts is delta-neutral):
        phi[k] =  - num_puts * put.delta_put(current_stock_price=S[k], time_to_maturity=T - time[k])
        # buy calls to compensate for the gamma, then change phi i.o.t. compensate for the extra delta
        gamma_put = put.gamma_put(current_stock_price=S[k], time_to_maturity=T - time[k])
        gamma_portfolio = num_puts * gamma_put
        gamma_call = call.gamma_call(current_stock_price=S[k], time_to_maturity=T_call - time[k])
        calls[k] = - gamma_portfolio/gamma_call
        delta_call = call.delta_call(current_stock_price=S[k], time_to_maturity=T_call - time[k])
        extra_delta = calls[k] * delta_call
        phi[k] = phi[k] - extra_delta
        # determine new position B, such that there is no net cashflow in (S, B)-portfolio:
        psi[k] = (value - phi[k] * S[k]) / B[k]
        # mismatch between discrete-time delta-neutral, self-financing portfolio and price puts:
        total_portfolio_value[k] = price_puts[k] + phi[k] * S[k] + psi[k] * B[k]
    return time, S, B, phi, psi, price_puts, total_portfolio_value

time, S, B, phi, psi, price_puts, total_portfolio_value = writing_put_option_delta_gamma_hedge_discrete_time(K, T, S_0, mu, sigma,B_0, r, num_puts)
print("initial position in stock: " + str(phi[0]))
print("initial position in money market account: " + str(psi[0]))

# preallocating
sims_S = np.zeros((1,int(T/time_delta)+1))
sims_B = np.zeros((1,int(T/time_delta)+1))
sims_phi = np.zeros((1,int(T/time_delta)+1))
sims_psi = np.zeros((1,int(T/time_delta)+1))
sims_price_puts = np.zeros((1,int(T/time_delta)+1))
sims_total_portfolio_value = np.zeros((1,int(T/time_delta)+1))
sims_gamma = np.zeros((1,int(T/time_delta)+1))

put = BlackScholesOptionPrice(K, r, sigma)
call = BlackScholesOptionPrice(K_call, r, sigma)
all_gammas = np.zeros((1,int(T/time_delta)+1))

for sim in range(M):
    print("Simulation:" + str(sim), end = '\r')
    time, S, B, phi, psi, price_puts, total_portfolio_value = writing_put_option_delta_gamma_hedge_discrete_time(K, T, S_0, mu, sigma,
                                                              B_0, r, num_puts)
    gammas = np.array([])
    
    # calculate gamma for each point in time
    for i in range(len(S)):
        current_stock_price = S[i]
        current_time = time[i]
        current_time_to_maturity = T - current_time
        gamma = put.gamma_put(current_stock_price, current_time_to_maturity)
        gammas = np.append(gammas, gamma)

    gammas = gammas.reshape(1,-1)    
    all_gammas = np.r_[all_gammas,gammas]

    # store simulated results    
    S = S.reshape(1,-1)
    sims_S = np.r_[sims_S, S]
    B = B.reshape(1,-1)
    sims_B = np.r_[sims_B, B]
    phi = phi.reshape(1,-1)
    sims_phi = np.r_[sims_phi, phi]
    psi = psi.reshape(1,-1)
    sims_psi = np.r_[sims_psi, psi]
    price_puts = price_puts.reshape(1,-1)
    sims_price_puts = np.r_[sims_price_puts, price_puts]
    total_portfolio_value = total_portfolio_value.reshape(1,-1)
    sims_total_portfolio_value = np.r_[sims_total_portfolio_value, total_portfolio_value]

# remove first row of zeros
sims_S = sims_S[1:]
sims_B = sims_B[1:]
sims_phi = sims_phi[1:]
sims_psi = sims_psi[1:]
sims_price_puts = sims_price_puts[1:]
sims_total_portfolio_value = sims_total_portfolio_value[1:]
all_gammas = all_gammas[1:]
 
# preallocate for quantiles
percentiles_phi_5 = np.zeros((int(T/time_delta)+1))
percentiles_phi_50 = np.zeros((int(T/time_delta)+1)) 
percentiles_phi_95 = np.zeros((int(T/time_delta)+1))

percentiles_psi_5 = np.zeros((int(T/time_delta)+1))
percentiles_psi_50 = np.zeros((int(T/time_delta)+1)) 
percentiles_psi_95 = np.zeros((int(T/time_delta)+1))

percentiles_gamma_5 = np.zeros((int(T/time_delta)+1))
percentiles_gamma_50 = np.zeros((int(T/time_delta)+1)) 
percentiles_gamma_95 = np.zeros((int(T/time_delta)+1))

# calculate quantiles
for j in range(int(T/time_delta)+1):
    perc5 = np.percentile(sims_phi[:,j], 5)
    perc50 = np.percentile(sims_phi[:,j], 50)
    perc95 = np.percentile(sims_phi[:,j], 95)
    
    percentiles_phi_5[j] = perc5
    percentiles_phi_50[j] = perc50
    percentiles_phi_95[j] = perc95

    perc5 = np.percentile(sims_psi[:,j], 5)
    perc50 = np.percentile(sims_psi[:,j], 50)
    perc95 = np.percentile(sims_psi[:,j], 95)
    
    percentiles_psi_5[j] = perc5
    percentiles_psi_50[j] = perc50
    percentiles_psi_95[j] = perc95

    perc5 = np.percentile(all_gammas[:,j], 5)
    perc50 = np.percentile(all_gammas[:,j], 50)
    perc95 = np.percentile(all_gammas[:,j], 95)
    
    percentiles_gamma_5[j] = perc5
    percentiles_gamma_50[j] = perc50
    percentiles_gamma_95[j] = perc95

# plot the new values
x = np.arange(0,int(T/time_delta)+1)
plt.xlabel("Time")
plt.ylabel("Percentile Values")
plt.title("Simulations of psi")
plt.plot(x,percentiles_psi_5, label = '5th quantile psi')
plt.plot(x,percentiles_psi_50, label = '50th quantile psi')
plt.plot(x,percentiles_psi_95, label = '95th quantile psi')
plt.legend(loc = "upper right")
plt.show()

plt.xlabel("Time")
plt.ylabel("Percentile Values")
plt.title("Simulations of phi")
plt.plot(x,percentiles_phi_5, label = '5th quantile phi')
plt.plot(x,percentiles_phi_50, label = '50th quantile phi')
plt.plot(x,percentiles_phi_95, label = '95th quantile phi')
plt.legend(loc = "upper right")
plt.show()

plt.xlabel("Time")
plt.ylabel("Percentile Values")
plt.title("Simulations of gamma")
plt.plot(x,percentiles_gamma_5, label = '5th quantile gamma')
plt.plot(x,percentiles_gamma_50, label = '50th quantile gamma')
plt.plot(x,percentiles_gamma_95, label = '95th quantile gamma')
plt.legend(loc = "upper right")
plt.show()

mean_total_portfolio_value_maturity = np.mean(sims_total_portfolio_value[:,-1])
print("mean value of the total portfolio is" + str(mean_total_portfolio_value_maturity))
std_total_portfolio_value_maturity = np.std(sims_total_portfolio_value[:,-1])
print("standard deviation of the total portfolio is" + str(std_total_portfolio_value_maturity))
 
price_put = put.price_put(S_0, T)
print("price of the put is" + str(price_put))
print("price of the 1000 puts is " + str(price_put*num_puts))

price_call = call.price_call(S_0, T_call)
print("price of the call is" + str(price_call))