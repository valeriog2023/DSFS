#! /usr/bin/env python
import sys
import os
current_path = os.path.abspath(".")
sys.path.append(f"{current_path}/ch4/")
from vector import Vector,distance
from tqdm import tqdm
from matplotlib import pyplot as plt
from typing import List

# the higher the number of dimensions in the dataset
# the bigger the problems get with K neareset neighbours
# the reason is that points tend to be more sparse/distant
# as the number of dimensions increase
import random

def random_point(dim: int) -> Vector:
    """This function generates a point of dimension dim
       with random values between 0 and 1
    """
    return [ random.random() for _ in range(dim) ]


def random_distances(dim: int, num_pairs: int)-> List[float]:
    """This function takes as input:
       dim: <int> the number of dimension we want to consider for each point
       num_pairs: <int> the number of pairs of random points we want to generate

       it will return the list of distances between each pair of random points generated 
    """
    return [ distance(random_point(dim), random_point(dim)) 
             for _ in range(num_pairs) ]


# now we test with num_pairs point (10000)
# and witha number of dimensions increasing from 1 to max_dimension 101
max_dimensions = 101
num_points = 10000


avg_distances = []
min_distances = []

random.seed(0)
for dim in tqdm(range(max_dimensions), desc="Curse of Dimensionality"):
    distances = random_distances(dim,num_points)
    avg_distances.append(sum(distances)/num_points)
    min_distances.append(min(distances))

# Data for plotting
fig, ax = plt.subplots()
ax.plot(range(max_dimensions), avg_distances, linestyle='dotted', label="average distance")
ax.plot(range(max_dimensions), min_distances, label="minimum distance")

ax.set(xlabel='# of dimensions', ylabel='Distance',
       title=f'{num_points:,} Random Distances')
ax.grid()
fig.set_figheight(10)
fig.set_figwidth(12)
plt.legend(loc='best')
plt.show()    