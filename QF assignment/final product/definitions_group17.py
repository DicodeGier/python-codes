import numpy as np
from scipy.stats import norm

np.random.seed(1)

# the following class was taken from github, where we added the gamma_put (and gamma_call which is the same) function
class BlackScholesOptionPrice():
    """Class for Black-Scholes price of European put and call options."""

    def __init__(self, strike: float, r: float, sigma: float):
        
        self.r = r
        self.sigma = sigma
        self.strike = strike

    def _d1_and_d2(self, current_stock_price, time_to_maturity):
        """Calculates auxiliary d_1 and d_2 which enter the N(0, 1) cdf in the pricing formulas"""
        
        d1 = (np.log(current_stock_price / self.strike) + (self.r + 0.5 * self.sigma ** 2) * time_to_maturity) / (self.sigma * np.sqrt(time_to_maturity))
        d2 = d1 - self.sigma * np.sqrt(time_to_maturity)
        return d1, d2

    def price_put(self, current_stock_price, time_to_maturity):
        """Calculates price of European put option"""

        d1, d2 = self._d1_and_d2(current_stock_price, time_to_maturity)
        return np.exp(-self.r * time_to_maturity) * self.strike * norm.cdf(-d2) - current_stock_price * norm.cdf(-d1)
    
    def delta_put(self, current_stock_price, time_to_maturity):
        """Calculates delta of European put option."""
        
        d1, _ = self._d1_and_d2(current_stock_price, time_to_maturity)
        return - norm.cdf(- d1)
                
    def price_call(self, current_stock_price, time_to_maturity):
        """Calculates price of European call option"""

        d1, d2 = self._d1_and_d2(current_stock_price, time_to_maturity)
        return current_stock_price * norm.cdf(d1) - np.exp(-self.r * time_to_maturity) * self.strike *  norm.cdf(d2)
    
    def delta_call(self, current_stock_price, time_to_maturity):
        """Calculates delta of European call option."""
        
        d1, _ = self._d1_and_d2(current_stock_price, time_to_maturity)
        return norm.cdf(d1)
    
    def _vega(self, current_stock_price, time_to_maturity):
        """Computes vega."""
        
        d1, _ = self._d1_and_d2(current_stock_price, time_to_maturity)
        return current_stock_price * norm.pdf(d1) * np.sqrt(time_to_maturity)
    
    def vega_call(self, current_stock_price, time_to_maturity):
        return self._vega(current_stock_price, time_to_maturity)

    def vega_put(self, current_stock_price, time_to_maturity):
        return self._vega(current_stock_price, time_to_maturity)
    
    def gamma_put(self, current_stock_price, time_to_maturity):
        d1, _ = self._d1_and_d2(current_stock_price, time_to_maturity)
        return norm.pdf(d1)/(current_stock_price * self.sigma * np.sqrt(time_to_maturity))
    
    def gamma_call(self, current_stock_price, time_to_maturity):
        d1, _ = self._d1_and_d2(current_stock_price, time_to_maturity)
        return norm.pdf(d1)/(current_stock_price * self.sigma * np.sqrt(time_to_maturity))
    
def approximate_delta_put_bump_reprice_common_CI_delta(num_replications, S_0, T, sigma, r, K, h):
    # function used to calculate the delta and a confidence interval using bump and reprice and common random numbers
    option_prices = []
    option_prices_bumped = []
    for _ in range(num_replications):
        Z = np.random.normal(0,1)
        stock = np.zeros(T + 1)
        stock_bumped = np.zeros(T + 1)
        stock[0] = S_0
        stock_bumped[0] = S_0 + h
        for time in range(1, T + 1): 
            stock[time] = stock[time-1] * np.exp((r - 0.5 * sigma**2) + sigma * Z)
            stock_bumped[time] = stock_bumped[time-1] * np.exp((r - 0.5 * sigma**2) + sigma * Z)
        payoff = max(0, K - (1/T) * np.sum(stock))
        payoff_bumped = max(0, K - (1/T) * np.sum(stock_bumped))
        option_prices.append(payoff * np.exp(-r * T))
        option_prices_bumped.append(payoff_bumped * np.exp(-r * T))

    deltas = np.subtract(np.array(option_prices_bumped), np.array(option_prices)) / h
    mean_delta = np.mean(deltas)
    sigma_delta = np.std(deltas)
    confidence_level = 0.95
    z_score = norm.ppf((1 + confidence_level) / 2)

    LB = mean_delta - z_score * (sigma_delta / np.sqrt(num_replications))
    UB = mean_delta + z_score * (sigma_delta / np.sqrt(num_replications))
    return mean_delta, LB, UB 

def approximate_delta_put_bump_reprice_noncommon_CI_delta(num_replications, S_0, T, sigma, r, K, h):
    # function used to calculate the delta and a confidence interval using bump and reprice and independent random numbers
    option_prices = []
    option_prices_bumped = []
    for _ in range(num_replications):
        Z = np.random.normal(0,1)
        Z_bumped = np.random.normal(0,1)
        stock = np.zeros(T + 1)
        stock_bumped = np.zeros(T + 1)
        stock[0] = S_0
        stock_bumped[0] = S_0 + h
        for time in range(1, T + 1): 
            stock[time] = stock[time-1] * np.exp((r - 0.5 * sigma**2) + sigma * Z)
            stock_bumped[time] = stock_bumped[time-1] * np.exp((r - 0.5 * sigma**2) + sigma * Z_bumped)
        payoff = max(0, K - (1/T) * np.sum(stock))
        payoff_bumped = max(0, K - (1/T) * np.sum(stock_bumped))
        option_prices.append(payoff * np.exp(-r * T))
        option_prices_bumped.append(payoff_bumped * np.exp(-r * T))

    deltas = np.subtract(np.array(option_prices_bumped), np.array(option_prices)) / h
    mean_delta = np.mean(deltas)
    sigma_delta = np.std(deltas)
    confidence_level = 0.95
    z_score = norm.ppf((1 + confidence_level) / 2)

    LB = mean_delta - z_score * (sigma_delta / np.sqrt(num_replications))
    UB = mean_delta + z_score * (sigma_delta / np.sqrt(num_replications))
    return mean_delta, LB, UB
    

def approximate_delta_put_bump_reprice_common(num_replications, S_0, T, sigma, r, K, h):
    # function used to calculate the delta using bump and reprice and common random numbers
    # taken from github for the case of vega and adjusted for delta
    W_Q_T = np.sqrt(T) * norm.rvs(size=num_replications)
    S_T =  S_0 * np.exp((r - 0.5 * sigma ** 2) * T + sigma * W_Q_T)
    option_price_prox = np.exp(-r * T) * np.mean(np.maximum(K - S_T, 0))
    S_T_bump =  (S_0 + h) * np.exp((r - 0.5 * sigma ** 2) * T + sigma * W_Q_T)
    option_price_prox_bump = np.exp(-r * T) * np.mean(np.maximum(K - S_T_bump, 0))
    return (option_price_prox_bump - option_price_prox) / h 


def approximate_delta_put_pathwise_common(num_replications, S_0, T, sigma, r, K):
    # function used to calculate the delta using the pathwise method
    sum = 0
    counter = 1
    while counter <= num_replications:
        W_Q_T = np.sqrt(T) * norm.rvs(size=1)
        S_T =  S_0 * np.exp((r - 0.5 * sigma ** 2) * T + sigma * W_Q_T)
        if S_T < K:
            pathwise_indicator = 1
        else:
            pathwise_indicator = 0
        approx = pathwise_indicator * np.exp((r - 0.5 * sigma ** 2) * T + sigma * W_Q_T)
        sum = sum + approx
        counter = counter + 1
    return float(sum/num_replications)

def approximate_delta_put_likelihood_ratio_common(num_replications, S_0, T, sigma, r, K):
    # function used to calculate the delta using the likelihood ratio method
    sum = 0
    counter = 1
    while counter <= num_replications:
        W_Q_T = np.sqrt(T) * norm.rvs(size=1)
        S_T =  S_0 * np.exp((r - 0.5 * sigma ** 2) * T + sigma * W_Q_T)
        if S_T < K:
            likelihood_indicator = 1
        else:
            likelihood_indicator = 0
        log_derivative_S_0 = (np.log(S_T/S_0) - (r - 0.5 * sigma ** 2) * T)/(sigma ** 2 * T * S_0)
        approx = np.exp(-r * T) * likelihood_indicator * (K-S_T) * log_derivative_S_0
        sum = sum + approx
        counter = counter + 1
    return float(sum/num_replications)

 
def approximate_gamma_put_bump_and_reprice_common(num_replications, S_0, T, sigma, r, K, h):
    # function used to calculate the gamma using bump and reprice and common random numbers
    W_Q_T = np.sqrt(T) * norm.rvs(size=num_replications)
    S_T =  S_0 * np.exp((r - 0.5 * sigma ** 2) * T + sigma * W_Q_T)
    option_price_prox = np.exp(-r * T) * np.mean(np.maximum(K - S_T, 0))
    S_T_bump_up =  (S_0 + h) * np.exp((r - 0.5 * sigma ** 2) * T + sigma * W_Q_T)
    option_price_prox_bump_up = np.exp(-r * T) * np.mean(np.maximum(K - S_T_bump_up, 0))
    S_T_bump_down =  (S_0 - h) * np.exp((r - 0.5 * sigma ** 2) * T + sigma * W_Q_T)
    option_price_prox_bump_down = np.exp(-r * T) * np.mean(np.maximum(K - S_T_bump_down, 0))

    return (option_price_prox_bump_up - 2* option_price_prox + option_price_prox_bump_down) / h ** 2

def approximate_gamma_put_likelihood_ratio_common(num_replications, S_0, T, sigma, r, K):
    # function used to calculate the gamma using the likelihood ratio method and common random numbers
    sum = 0
    counter = 1
    while counter <= num_replications:
        W_Q_T = np.sqrt(T) * norm.rvs(size=1)
        S_T =  S_0 * np.exp((r - 0.5 * sigma ** 2) * T + sigma * W_Q_T)
        if S_T < K:
            likelihood_indicator = 1
        else:
            likelihood_indicator = 0
        log_derivative_S_0 = (-1 - np.log(S_T) + np.log(S_0) + (r - 0.5 * sigma ** 2) * T)/(sigma ** 2 * T * S_0 ** 2)
        approx = np.exp(-r * T) * likelihood_indicator * (K-S_T) * log_derivative_S_0
        sum = sum + approx
        counter = counter + 1
    return float(sum/num_replications)


    