######################################################################
# If the data  shows vairation across a dimension more than others
# we can use an approach for dimensionality reduction
# the technique is called:
#
# Principal component analysis
#
# and it is used to extract one or more dimensions that capture as
# much of the variation as possible
# In the example here we only use 2 dimensions.. and in reality we would ont use PCA..
# it's probably more likely to be used when you have a lot more dimensions
import sys
sys.path.append("ch4/")
from vector import subtract,Vector, vector_mean, magnitude, dot
from typing import List

def de_mean(data:List[Vector], verbose:bool=False) -> List[Vector]:
    """Returns the Lit of Vectors
       where every value has been computed by subtracting the mean for that dimension
       e.g.
        [ [1,2,3], [3,2,1], [1,1,1], [3,3,3] ]
        it has 3 dimensions (4 points/vectors)
         1  2  3
         3  2  1
         1  1  1
         3  3  3
        the mean is the same for all dimensions in this case = 2
        so will return
       [[-1, 0, 1], [1, 0, -1], [-1, -1, -1], [1, 1, 1]]
    """
    mean = vector_mean(data)
    if verbose:
        print(f"Data is {data}")
        print(f"Mean is { mean }")

    return [subtract(vector,mean) for vector in data]


vectors = [ [1,2,3], [3,2,1], [1,1,1], [3,3,3] ]
assert de_mean(vectors) == [[-1.0, 0.0, 1.0], [1.0, 0.0, -1.0], [-1.0, -1.0, -1.0], [1.0, 1.0, 1.0]]

#
# now we want to get which direction gets most of the variation
# i.e. given a vector d of magnitude 1
# the projection of the data vector over d is given by the dot product
#
# Note the projection of v over u is given by
#              u dot v
# Proj_u(v) = --------- * u  -> if the magnitude of u is one, then (u dot v) u
#              || u ||**2
# Note: remember u dot v is a scalar
#
def direction(w: Vector)->Vector:
    """
    Returns a direction of magnitude one in the direction of the vector w
    """
    mag = magnitude(w)
    return [ w_i / mag for w_i in w ]


def directional_variance(data: List[Vector], w:Vector) -> float:
    """
    Returns the variance of the data in the direction of w
    This is actually the square of the projection f each vector in the w direction
    all summed together
    """
    w_dir = direction(w)
    return sum(dot(v,w_dir)**2 for v in data)



def directional_variance_gradient(data:List[Vector], w:Vector) -> Vector:
    """
    This gives the gradient of directional variance with respect to w
    """
    w_dir = direction(w)
    return [ sum(2 * dot(v, w_dir))]

#
# stopping here for the moment..
# this requires lagrange multipliers and eigenvectors/eigen values
