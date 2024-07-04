mu = 0.1
sigma = 0.25
S_0 = 100
B_0 = 1
r = 0.03
K = 100
T = 2
#Put option

from definitions import *

###question a
put = BlackScholesOptionPrice(K, r, sigma)
#exact
delta = put.delta_put(current_stock_price=S_0, time_to_maturity=T)
print(delta)

n = 100000
h = 0.0001
#bump & reprice
put_delta_bump_reprice = approximate_delta_put_bump_reprice_common(n, S_0, T, sigma, r, K, h)
print(put_delta_bump_reprice)

#pathwise method
put_delta_pathwise = approximate_delta_put_pathwise_common(n, S_0, T, sigma, r, K)
print(put_delta_pathwise)

#likelihood ratio
put_delta_likelihood_ratio = approximate_delta_put_likelihood_ratio_common(n, S_0, T, sigma, r, K)
print(put_delta_likelihood_ratio)
