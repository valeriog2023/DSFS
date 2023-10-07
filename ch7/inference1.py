from typing import Tuple
import math
from scipy.stats import norm

def normal_approximation_to_binomial(n: int, p: float)-> Tuple[float,float]:
    """Returns the value of mu and sigma of a normal deviation function that matches 
       the binomial distribution with paramters n and p
    """
    mu = p * n # this is the expected value of the binomial distribution
    sigma = math.sqrt( n * p * (1-p))
    return mu,sigma


def normal_probability_below(z:float, mu:float=0, sigma:float=1) -> float:
    """
    Returns the probability that x < Z for a normal distribution of mu: mu and sigma: sigma
    """
    return norm(mu,sigma).cdf(z)

def normal_probability_above(z:float, mu:float=0, sigma:float=1) -> float:
    """
    Returns the probability that x > Z for a normal distribution of mu: mu and sigma: sigma
    """
    return norm(mu,sigma).sf(z)


def normal_probability_between(z_low:float, z_high:float, mu:float=0, sigma:float=1) -> float:
    """
    Returns the probability that Z_high > x > Z_low for a normal distribution of mu: mu and sigma: sigma
    """
    return normal_probability_below(z_high,mu,sigma) - normal_probability_below(z_low,mu,sigma)


def normal_probability_outside(z_low:float, z_high:float, mu:float=0, sigma:float=1) -> float:
    """
    Returns the probability that Z_high > x > Z_low for a normal distribution of mu: mu and sigma: sigma
    """
    return 1 - normal_probability_between(z_low, z_high, mu, sigma)


print("Testing basic assert on normal_probability_below and normal_probability_above")
assert normal_probability_below(0) == normal_probability_above(0) == 0.5
assert normal_probability_below(0.3) + normal_probability_above(0.3) == 1
assert normal_probability_below(0.5) + normal_probability_above(0.5) == 1
assert normal_probability_below(0.9) + normal_probability_above(0.9) == 1
assert normal_probability_below(-1) + normal_probability_above(-1) == 1
print("done!")
