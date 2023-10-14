from typing import Tuple
import math
import random
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

def normal_two_sided_bounds(p_range: float, mu:float =0, sigma:float=1) -> (float,float):
    """Returns the z lower/upper values for which P(Z>=z>=-Z) == p
       This is the Z value around the mean

       Note: it's Z values if mu=0 and sigma = 1
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
#
#   P values
#
print("\n\n---------\nTest P values")
def two_sided_p_value(x: float, mu:float=0, sigma:float=1) -> float:
    """
    this function returns the probability value given the result of a test and
    a value for mu (default=0) and sigma (default=1)
    i.e
    given a mu,sigma what is the probability to get a result as extreme as x (both above and below the mean) ?
    if x == mu it will return 1
    """
    if x > mu:
        return 2 * normal_probability_above(x,mu,sigma)
    elif x < mu:
        return 2 * normal_probability_below(x,mu,sigma)
    else:
        return 1

binomial_mu, binomial_sigma = normal_approximation_to_binomial(1000,0.5)
test_result = 529.5
p_value_for_test = two_sided_p_value(test_result,binomial_mu,binomial_sigma)
p_value_for_test_percent = p_value_for_test * 100
print(f"P value for mu: {binomial_mu} and sigma: {binomial_sigma} and a test result of { test_result } is: {p_value_for_test}")
print("Note sa we used a non integer value for the test result.. \nthis is because the normal distribution is only an approximiation for the binomial distribution")
print("So in this case, we assume the result was 530 and we adopted a continuity correction and set it to 529.5")

print("\n\n we now run a simulation..")
tests_number = 1000
print(f"Now we generate {tests_number} test of 1000 throws and verify what p value we would get for the same test result; i.e. a result as extreme as 530 above/below mu(500)")
extreme_value_count = 0
for _ in range(tests_number):
    num_heads = sum(1 if random.random() <0.5 else 0 for _ in range(1000))
    if num_heads < 470 or num_heads > 530:
        extreme_value_count += 1

print(f"Simulation result, extreme values count is: {extreme_value_count}")
print(f"we expect to get a value as exterme in {p_value_for_test_percent} of the cases.. so on {tests_number} this should be around {round(tests_number*p_value_for_test)}")
print("If the p value is greater than the significance level, we don't reject H0")
print("Now we try with a test result of 540")
test_result = 540
p_value_for_test = two_sided_p_value(test_result,binomial_mu,binomial_sigma)
p_value_for_test_percent = p_value_for_test * 100
print(f"P value is : {p_value_for_test} which is smaller than alfa (Assuming that's 5%) so we can reject H0")
print("\n\n we now run the simulation again simulation..")
tests_number = 1000
print(f"Now we generate {tests_number} test of 1000 throws and verify what p value we would get for the same test result; i.e. a result as extreme as 530 above/below mu(500)")
extreme_value_count = 0
for _ in range(tests_number):
    num_heads = sum(1 if random.random() <0.5 else 0 for _ in range(1000))
    if num_heads < 460 or num_heads > 540:
        extreme_value_count += 1
print(f"On {tests_number} tests we got a results that extreme {extreme_value_count} times")        

