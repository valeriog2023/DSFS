from typing import List
import random
from inference1 import normal_approximation_to_binomial,normal_two_sided_bounds
import os
import math
os.system('clear')

binomial_mu, binomial_sigma = normal_approximation_to_binomial(1000,0.5)


def run_experiment(N:int=1000) -> List[bool]:
    """Flips a fair coin N amount times (default 1000, True = heads, False = tails)"""
    return [random.random() < 0.5 for _ in range(N)]


def reject_fairness(experiment: List[bool], significance_level:float=0.05) -> bool:
    """Given the result of run_experiment, i.e. a list of bool
       and a significance level (default 5% , i.e. 0.05)
       it willr return True if it rejects the H0 i.e. we believe the coin is not fair
    """
    num_heads = len([result for result in experiment if result])
    num_flips = len(experiment)
    p_hat = num_heads/num_flips
    confidence_level = 1 - significance_level
    sigma_hat = math.sqrt( (p_hat * (1 - p_hat))/num_flips )
    lower_bound,upper_bound = normal_two_sided_bounds(confidence_level, p_hat, sigma_hat)
    return 0.5 > upper_bound or 0.5 < lower_bound

print("Running 1000 experiments and checking how many time we reject H0 even if it is true with confidence level of 0.95")
random.seed(0)
experiments =  [ run_experiment() for _ in range(1000)]
num_rejections = len(['rejected' for experiment in experiments if reject_fairness(experiment)] )

print(f"Valid H0 Rejected: {num_rejections} times out of 1000")