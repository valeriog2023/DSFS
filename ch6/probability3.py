import math
import matplotlib.pyplot as plt
import numpy

SQRT_TWO_PI = math.sqrt(2 * math.pi)

def normal_pdf(x: float, mu:float = 0, sigma: float = 1) -> float:
    return (math.exp(- (((x-mu)/sigma)**2 )/2) ) / ( SQRT_TWO_PI * sigma )


xs = numpy.arange(-5,5,0.1)
y1_values = [ normal_pdf(x) for x in xs ]
y2_values = [ normal_pdf(x,sigma=2) for x in xs ]
y3_values = [ normal_pdf(x,sigma=0.5) for x in xs ]
y4_values = [ normal_pdf(x,mu=-1) for x in xs ]
plt.plot(xs,y1_values, '-', label='mu=0, sigma=1')
plt.plot(xs,y2_values, '--', label='mu=0, sigma=2')
plt.plot(xs,y3_values, ':', label='mu=0, sigma=0.5')
plt.plot(xs,y4_values, '-,', label='mu=-1, sigma=1')
plt.title("Normal distribution")
plt.legend(loc='best')
plt.show()
