import random, numpy as np
from matplotlib import pyplot as plt

random.seed(0)

def uniform_pdf(x:float) -> float:
    '''probability of a value in uniform distribution is 1/N where N is the events space
       if N is infinite the probability is zero for any specific event
       Total area under the curve is one
    '''
    return 1 if 0 <= x < 1 else 0


def uniform_cdf(x:float) -> float:
    '''Returns the probability that a uniform random variable is <= x
       Total area under the curve is one
    '''
    if x < 0: return 0    # probability is defined ony between 0 and 1
    elif x < 1: return x  # probability that X < x is x
    else: return 1        # probability max value is 

points = np.arange(-1.0 ,2.0,0.01)
pdf_values = [ uniform_pdf(float(x)) for x in points ]
cdf_values = [ uniform_cdf(float(x)) for x in points ]

plt.plot(points,pdf_values, 'g',  label='pdf')    # green solid line
plt.plot(points,cdf_values, 'r', label = 'cdf')    # red solid line
plt.title("Uniform Distribution - PDF / CDF")
plt.legend(loc='best')
plt.show()


