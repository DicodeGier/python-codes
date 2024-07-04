import itertools
import math

def shapley_value(n, v):
    shapley_vals = [0] * n
    factorial = [math.factorial(i) for i in range(n + 1)]
    N = set(range(n))
    
    for i in range(n):
        for S in itertools.chain.from_iterable(itertools.combinations(N - {i}, r) for r in range(n)):
            S = set(S)
            S_with_i = S | {i}
            marginal_contrib = v(S_with_i) - v(S)
            weight = factorial[len(S)] * factorial[n - len(S) - 1] / factorial[n]
            shapley_vals[i] += weight * marginal_contrib
    
    return shapley_vals

# Define the characteristic function for a sample simple game
def v(S):
    # Example: Winning coalitions are those with more than 4 players
    if len(S) > 6 and 0 in S and 1 in S and 2 in S and 3 in S:
        return 1 
    else: 
        return 0

# Number of players
n = 9

# Calculate Shapley values
shapley_vals = shapley_value(n, v)
print("Shapley Values:", shapley_vals)