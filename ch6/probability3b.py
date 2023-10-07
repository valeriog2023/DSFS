import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


# ppf(q) -> gives the z value given the probability
# >>> norm.ppf(0.01)
# -2.3263478740408408
# >>> norm.ppf(0.5)
# 0.0
# Also works for multiple values
#>>> norm.ppf([0.025,0.975])
#array([-1.95996398,  1.95996398])
#
# opposite is norm.cdf -> gives the probability given the z value
# >>> norm.cdf(0)
# 0.5
#>>> norm.cdf(1)    -> also works for multiple values
#array([0.15865525, 0.84134475])




x1 = np.linspace(norm.ppf(0.01), norm.ppf(0.99), 100)
x2 = np.linspace(-3.0, 3.0, 300)
fig, (ax1,ax2) = plt.subplots(1, 2)
ax1.plot(x1, norm.pdf(x1), 'r-', lw=3, alpha=0.6, label='norm pdf')
ax2.plot(x2, norm.cdf(x2), 'b-', lw=3, alpha=0.6, label='norm cdf')
fig.suptitle("PPF and CDF")
ax1.legend(loc='best')
ax2.legend(loc='best')

plt.show()