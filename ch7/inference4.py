from typing import Tuple
from inference1 import two_sided_p_value
import os
os.system("clear")
import math
msg="""
#
# TESTS ON DIFFERENCE OF DISTRIBUTIONs
# A/B Tests for Bernoulli/Binomial
# the mu of the diff is given by the diff of the means and
# the variance is given by the sum of the variances i.e. sqrt( sigma_A^2 + sigma_B^2 )
#
# H0 usually assumes that there is no difference between A and B
# so that mu of the diff is zero (same for p)
"""
print(msg)

def estimated_parameters(N:int, n: int) -> Tuple[float,float]:
    """the function takes N (sample size) and n number of success in the sample
       and returns the tuple done by
       p^ = n/N
       and
       sigma^ = math.sqrt( p^ * (1-p^) / N)

    """
    p = n/N
    sigma = math.sqrt( p * (1-p) / N)
    return p, sigma


def a_b_test_statistic(N_A: int, n_A:int, N_B:int, n_B: int)-> float:
    """
    Returns Z value for the difference of teh results assuming it's due to chance only
    Note: we assume they are all normal distribution and that the sample size is big enough

    the Z value is given by  p_A^ - p_B^ - (p_A-p_B which we assume are the same if H0 is valid)
    divided by the sigma of the distribution of the differences i.e. sqrt( sigma_A^2 + sigma_B^2 )
    """
    p_A,sigma_A = estimated_parameters(N_A,n_A)
    p_B,sigma_B = estimated_parameters(N_B,n_B)
    return (p_A-p_B) / math.sqrt(sigma_A**2 + sigma_B**2)


z = a_b_test_statistic(1000,200,1000,180)

print(f"Test A statstic: {estimated_parameters(1000,200)}")
print(f"Test B statstic: {estimated_parameters(1000,180)}")
print(f"Test statstic result: {z} for diff of two tests (sample size: 1000) and success A:200, success B: 180")
print(f"The probability to get this Z value is: {two_sided_p_value(z)}")

z = a_b_test_statistic(1000,200,1000,150)
print("\nRepeating the test with different results")
print(f"Test A statstic: {estimated_parameters(1000,200)}")
print(f"Test B statstic: {estimated_parameters(1000,150)}")
print(f"Test statstic result: {z} for diff of two tests (sample size: 1000) and success A:200, success B: 150")
print(f"The probability to get this Z value is: {two_sided_p_value(z)}")