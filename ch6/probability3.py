import math
import matplotlib.pyplot as plt
import numpy

SQRT_TWO_PI = math.sqrt(2 * math.pi)

def normal_pdf(x: float, mu:float = 0, sigma: float = 1) -> float:
    return (math.exp(- (((x-mu)/sigma)**2 )/2) ) / ( SQRT_TWO_PI * sigma )


def normal_cdf(x: float, mu:float = 0, sigma: float =1) -> float:
    return (1+ math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


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
plt.show()
