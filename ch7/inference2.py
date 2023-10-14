from inference1 import normal_two_sided_bounds
import os
import random
import math
os.system('clear')
text_intro="""
#
# CONFIDENCE INTERVAL
#
# if we use the sampling distribution to get the paramters p_hat/mu_hat/sigma_hat
# we can build under certain assumptions a confidence interval
# the interval generated will capture the actual paramters with a certain level of confidence
# that can be decided in advance let's say 95% i.e. this means that the interfval
# created on 100 different samples will capture the actual parameters around 95 times

"""
tests_number = 1000
sample_size = 1000
actual_p = 0.5
expected_mu = actual_p * sample_size
significance_level = 0.05
confidence_level =  1 - significance_level


print(text_intro)
population_parameter_captured = 0

for i in range(tests_number):
    print(f"----- TEST {i:3} START")
    heads = sum(1 if random.random()>0.5 else 0 for _ in range(sample_size))
    p_hat = heads/sample_size
    sigma_hat = math.sqrt( (p_hat * (1 - p_hat))/sample_size )
    print(f"Got {heads} out of { sample_size}, p^ is {p_hat} and sigma^ is {sigma_hat}")    
    lower_bound,upper_bound = normal_two_sided_bounds(confidence_level, p_hat, sigma_hat)
    print(f"actual expected mu: {actual_p}, sample lower/upper bound: ({lower_bound}/{upper_bound})")
    if lower_bound < actual_p < upper_bound:
        population_parameter_captured += 1

print(f"\n----------\nRunning {tests_number} simulations with a smaple size of {sample_size} and a confidence level of {confidence_level}")
print(f"we captured the actual population paramter mu/p: {actual_p}, {population_parameter_captured} times i.e. {population_parameter_captured*100/tests_number}% of times")