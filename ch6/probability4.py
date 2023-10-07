import math
import matplotlib.pyplot as plt
import random
import numpy as np
from collections import Counter

SQRT_TWO_PI = math.sqrt(2 * math.pi)

def normal_pdf(x: float, mu:float = 0, sigma: float = 1) -> float:
    return (math.exp(- (((x-mu)/sigma)**2 )/2) ) / ( SQRT_TWO_PI * sigma )


def normal_cdf(x: float, mu:float = 0, sigma: float =1) -> float:
    return (1+ math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

def bernoulli_trial(p: float) -> int:
    """Returns 1 with probability p and 0 with probability 1-p"""
    return 1 if random.random() < p else 0

def binomial(n: int, p: float) -> int:
    """Returns the sum of N bernoulli(p) trials
    
       AS N get large a binomial distribution can be approximated with a normal distribution
       where mu = N*p and standard deviation = ( N*p*(1-p) )^0.5
    """
    return sum(bernoulli_trial(p) for _ in range(n))


def binomial_histogram(p:float, n: int, num_points: int) -> None:
    """Picks points from a Binomial(n,p) and plots thier histogram"""
    data = [ binomial(n, p) for _ in range(num_points)]

    # use a bar chart to show the actual binomial samples
    histogram = Counter(data)
    plt.bar([ x - 0.4 for x in histogram.keys() ],
            [ v / num_points for v in histogram.values() ],
            0.8,
            color='0.75'
            )
    
    mu = p * n
    sigma = math.sqrt(n * p * (1-p))
    xs = range(min(data), max(data) + 1)
    # y values are the area around the actual value.. in this case I take the area around the value +/- 0.5
    ys = [ normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma) for i in xs ] 
    plt.plot(xs,ys)
    plt.title("Binomial Distribution vs Normal Approximations")
    plt.show()


binomial_histogram(0.75, 100, 10000)

