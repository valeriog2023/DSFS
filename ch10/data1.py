from typing import List, Dict
from collections import Counter
import math
import random
import matplotlib.pyplot as plt
import sys
sys.path.append("/home/vale6811/Desktop/oreilly/DSFS/ch6/")
from probability3 import inverse_normal_cdf
from matplotlib import pyplot as plt

def bucketize(point: float, bucket_size:float) -> float:
    """Given a point P (float) and a bucket size B (float)
       This function returns the highest value, lower than the point P
       which is a multiple of B
       Basically it changes any contiuos number function into a step function
       where the step size is give by B
       Note here it uses the math function floo that return the integer part of a floor

        bucket_size * math.floor(point/bucket_size)
    """
    return bucket_size * math.floor(point/bucket_size)


def make_histogram(points: List[float], bucket_size: float) -> Dict[float,int]:
    """
    This function takes as input:
      points: A list of floats
      bucket_size: a float (size of a bucket)

      and it returns a dict where as key we have multiple of buckets (0, bucket, 2* bucket, etc..)
      and as value, the number of points in the bucket      
    """

    return Counter(bucketize(p,bucket_size) for p in points)


def plot_histogram(points: List[float], bucket_size: float, title: str=""):
    """This function creates an histogram with pyplot
       I takes as input a list of points and a bucket size
    """
    histogram_data = make_histogram(points, bucket_size)
    plt.bar([int(x) + (bucket_size/2) for x in histogram_data.keys()],    # x values we sum bucket_size/2, this s because the width is centered at this point
            histogram_data.values(),    # y values
            width= bucket_size-1        # width of the bars (we keep it a little smaller to have a nice sepration between the bars)
            )
    plt.title(title)
    plt.show()


#
# Let's create a list with random points between -100 and 100
uniform_distribution = [200 * random.random() - 100 for _ in range(10000)]
plot_histogram(uniform_distribution, 10, "Uniform Histogram")
##
#
# same but with normal distribution
normal_distribution = [57 * inverse_normal_cdf(random.random()) for _ in range(10000)]
plot_histogram(normal_distribution, 10, "Normal Histogram")
