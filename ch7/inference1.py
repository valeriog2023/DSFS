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


def normal_upper_bound(p: float, mu:float =0, sigma:float=1) -> float:
    """Returns the z value for which P(Z<=z) == p"""
    return norm(mu,sigma).ppf(p)

def normal_lower_bound(p: float, mu:float =0, sigma:float=1) -> float:
    """Returns the z value for which P(Z>=z) == p"""
    return norm(mu,sigma).ppf((1-p))

def normal_two_sided_bounds(p_range: float, mu:float =0, sigma:float=1) -> float:
    """Returns the z value for which P(Z>=z>=-Z) == p
       This is the Z value around the mean
    """
    #
    # probability of the tails; i.e. what is left outside of the range on either side
    tail_probability = (1 - p_range) / 2
    #
    # let's get the Z value for which we are above the lower tail
    lower_bound =  normal_upper_bound(tail_probability,mu,sigma)
    #
    # Note: the upper bound is symmetric but we can't just flip the sign because the symmetry is around the mean
    # and this function can work with non standard deviation where the mean is not zero so we need to actually
    # compute the upper_bound which is the max value for which we are undet the tail_probability
    upper_bound = normal_lower_bound(tail_probability,mu,sigma)
    #
    # return
    return lower_bound, upper_bound

print("Testing basic assert on normal_probability_below and normal_probability_above")
assert normal_probability_below(0) == normal_probability_above(0) == 0.5
assert normal_probability_below(0.3) + normal_probability_above(0.3) == 1
assert normal_probability_below(0.5) + normal_probability_above(0.5) == 1
assert normal_probability_below(0.9) + normal_probability_above(0.9) == 1
assert normal_probability_below(-1) + normal_probability_above(-1) == 1
assert normal_upper_bound(0.5) == 0
assert str(normal_upper_bound(0.99)).startswith('2.326')
assert normal_lower_bound(0.5) == 0
assert str(normal_lower_bound(0.99)).startswith('-2.326')
(b1,b2) = normal_two_sided_bounds(0.6827)
(b3,b4) = normal_two_sided_bounds(0.9545)
assert round(b1,4) == -1.0 and round(b2,4) == 1.0
assert round(b3,4) == -2.0 and round(b4,4) == 2.0
print("Test done!\n\n")
#
# fairness test on N=10000 throws of a coin (H/T p =0.5)
binomial_mu, binomial_sigma = normal_approximation_to_binomial(1000,0.5)
print(f"Binomial approximation to std mu, sigma: {binomial_mu}, {binomial_sigma}  for p == {0.5} and N = 1000\n")
#
# type 1 error: rejecting H0 even if H0 is correct
# if we consider a significance level of 5% we can find a range that contains 95% of the results
lower_b, upper_b = normal_two_sided_bounds(0.95, binomial_mu, binomial_sigma)
print(f"On 1000 throws of a fair coin and with a significance level of 5%\nwe reject the H0 hypothesis of fairness if we get a result outside\nthe following range: ({lower_b},{upper_b})")
print(f"\nNote: that even if outside our range, the event of being outside the range is possible and legit")
print(f"      this means that we will commit a type I error 5% of the times we use this approach")
#
# type 2 error: fail to reject H0 even if H0 is not correct
# Type II errors happen when the actual mean and sigma are different from the one used in H0
# however the value returned by the experiment is within the H0 distribution significance value 
# ranges
unfair_binomial_mu, unfair_binomial_sigma = normal_approximation_to_binomial(1000,0.55)  # here we have a higher p to get H (for instance)
#
# what is the probability to get a value between the range of the H0 distribution if I have the unfair distribution parameters?
type_2_p = normal_probability_between(lower_b,upper_b,unfair_binomial_mu,unfair_binomial_sigma)
print("The probability of a type II error (i.e. failing to reject H0 when it is false) depends on the mu,sigma of the actual distribution")
print("that, by hypothesis is different from H0 but not known")
print("In particular, how proabable is to get a value between the bounds set using H0 parameter if mu and sigma are different?")
print(f"For instance, if we assume p(H) == 0.55 then we can compute new mu, sigma: {unfair_binomial_mu}, {unfair_binomial_sigma}")
print(f"Probability to generate a value in the range: ({lower_b},{upper_b}) is {type_2_p}\n")
print(f"The probability of type II error gets lower if")
print(f"  - the real mu is far from the H0 mu")
print(f"  - N gets higher")
print(f"E.g.")
unfair_binomial_mu, unfair_binomial_sigma = normal_approximation_to_binomial(1000,0.6)  # here we have a higher p to get H (for instance)
type_2_p = normal_probability_between(lower_b,upper_b,unfair_binomial_mu,unfair_binomial_sigma)
print(f"p=0.6, N = 1000")
print(f"Probability to generate a value in the range: ({lower_b},{upper_b}) is {type_2_p}")
print("mu is more distant so the proability/overlapping of ranges gets much lower\n")
#
#
binomial_mu, binomial_sigma = normal_approximation_to_binomial(100,0.55)                # here we have a lower N so need to recompute mu and bounds
lower_b, upper_b = normal_two_sided_bounds(0.95, binomial_mu, binomial_sigma)
unfair_binomial_mu, unfair_binomial_sigma = normal_approximation_to_binomial(100,0.55)  # here we have a lower N so we need to recomute mu, sigma
type_2_p = normal_probability_between(lower_b,upper_b,unfair_binomial_mu,unfair_binomial_sigma)
print(f"p=0.55, N = 100")
print(f"Probability to generate a value in the range: ({lower_b},{upper_b}) is {type_2_p}")
print("N is much lower so mu and sigma are different (even for H0 the range is different). Also the overlapping gets much bigger with smaller N\n")

print("---- Finale note: Power is defined as 1 - p(typeII error)")