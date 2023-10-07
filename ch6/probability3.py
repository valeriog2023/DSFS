import math
import matplotlib.pyplot as plt
import numpy
from decimal import Decimal

SQRT_TWO_PI = math.sqrt(2 * math.pi)

def normal_pdf(x: float, mu:float = 0, sigma: float = 1) -> float:
    return (math.exp(- (((x-mu)/sigma)**2 )/2) ) / ( SQRT_TWO_PI * sigma )


def normal_cdf(x: float, mu:float = 0, sigma: float =1) -> float:
    return (1+ math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


def inverse_normal_cdf(p: float, mu: float = 0, sigma: float = 1, tolerance: float = 0.00001, verbose:bool = False) -> float:
    """
    This function will invert the cdf and return the probability value given a Z score
    It will use binary search to interate until the erro is under the tolerance value
    """

    # if not standard, compute standard and rescale
    if mu != 0  or sigma != 1:
        print("non standard distribution.. need to normalize")
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z = -10.0
    hi_z = 10.0
    if verbose: print(f"Start find Z for p: {p}")
    iteration = 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z ) / 2
        mid_p = normal_cdf(mid_z)
        if verbose: 
            print(f"------------------- iteration {iteration}")
            print(f"low_z: {low_z}")
            print(f"hi_z: {hi_z}")
            print(f"mid_z: {mid_z}")
            print(f"mid_p: {mid_p}")
        iteration =+ 1
        if mid_p == p:
            return Decimal(mid_z).quantize(Decimal('1e-6'))
        elif mid_p < p:
            low_z = mid_z
        else:
            hi_z = mid_z
    #
    return Decimal(mid_z).quantize(Decimal('1e-6'))

xs = numpy.arange(-5,5,0.1)
y11_values = [ normal_pdf(x) for x in xs ]
y12_values = [ normal_pdf(x,sigma=2) for x in xs ]
y13_values = [ normal_pdf(x,sigma=0.5) for x in xs ]
y14_values = [ normal_pdf(x,mu=-1) for x in xs ]

y21_values = [ normal_cdf(x) for x in xs ]
y22_values = [ normal_cdf(x,sigma=2) for x in xs ]
y23_values = [ normal_cdf(x,sigma=0.5) for x in xs ]
y24_values = [ normal_cdf(x,mu=-1) for x in xs ]

fig, (ax1,ax2) = plt.subplots(1, 2)
fig.suptitle("Normal PDF and CDF")
ax1.plot(xs,y11_values, '-', label='mu=0, sigma=1')
ax1.plot(xs,y12_values, '--', label='mu=0, sigma=2')
ax1.plot(xs,y13_values, ':', label='mu=0, sigma=0.5')
ax1.plot(xs,y14_values, '-,', label='mu=-1, sigma=1')
ax1.set_title("Various Normal PDFs")
ax2.plot(xs,y21_values, '-', label='mu=0, sigma=1')
ax2.plot(xs,y22_values, '--', label='mu=0, sigma=2')
ax2.plot(xs,y23_values, ':', label='mu=0, sigma=0.5')
ax2.plot(xs,y24_values, '-,', label='mu=-1, sigma=1')
ax2.set_title("Various Normal CDFs")
plt.legend(loc='best')

print(str(inverse_normal_cdf(0.01)))
print(str(inverse_normal_cdf(0.5)))
print(str(inverse_normal_cdf(1)))
assert inverse_normal_cdf(0.5) == 0
print("Passed assert check")

plt.show()

