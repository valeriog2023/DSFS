from typing import List, Dict
from collections import Counter
import math
import random
import matplotlib.pyplot as plt
import sys
sys.path.append("ch6/")
sys.path.append("ch3/")
from probability3 import inverse_normal_cdf
from statistics3 import standard_deviation
from matplotlib import pyplot as plt
from data1 import plot_histogram

def random_normal()-> float:
    """returns a random draw from a standard normal distribution"""
    return inverse_normal_cdf(random.random())

# this gives 1000 points randomly picked from a random normal distribution
xs = [ 100 * random_normal() for _ in range(1000)]
# this gets another draw of 1000 points and shifts it up of the previous value divided by 2
ys1 = [ ( x + 100 * random_normal()) / 2 for x in xs]
# this gets another draw of 1000 points, inverts the sign and shifts it up of the previous value (xs) divided by2
ys2 = [ (-x + 100 * random_normal()) / 2 for x in xs]

plot_histogram(xs,bucket_size=10,title="standard normal distribution")
plot_histogram(ys1,bucket_size=10,title="standard normal distribution shifted up")
plot_histogram(ys2,bucket_size=10,title="standard normal distribution inverted and shifted up")
print("They all look very similar but..")
plt.scatter(xs,ys1,marker='.',color='black',label='ys1')
plt.scatter(xs,ys2,marker='.',color='red',label='ys2')
plt.xlabel("xs")
plt.ylabel("ys")
plt.title("ys1 vs ys2 Distributions")
plt.legend(loc='best')
plt.show()
