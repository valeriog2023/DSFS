######################################################################
# If the data  shows variation across a dimension more than others
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
sys.path.append("ch8/")
from vector import subtract,Vector, vector_mean, magnitude, dot, scalar_multiply, subtract
from gradient_descent2 import gradient_step
import tqdm
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
    Each v is a point in a multidimensional space so we run the dot product
    in w direction (to get the component in that direction)
    The magintude of the move is 2*v[i] (derivative of variance which is quadaratic)

    The function returns, for each data vector v and direction w, a new vector which
    is the gradient in that data point  
    """
    w_dir = direction(w)
    return [ sum(2 * dot(v, w_dir) * v[i] ) for v in data  for i in range(len(w)) ]

#
# Now, in order to find the Principal component analysis we need to find the direction
# where we have the maximum of the variance
# the idea is that we can possibly reduce the dimensionality of the data and consider
# only the data covered in that direction or
# run the process multiple time:
# - find the principal comonent direction
# - remove the component in that direction
# - find the new principal componet direction in the remaining data
# - etc..

def first_principal_component(data: List[Vector],
                              n: int = 100,
                              step_size: float = 0.1) -> Vector:
    """This method runs a gradient descent from an aribtrary point/direction W with all 1.0 
       This is the initial direction that we use and against which we compute 
       the data variance 
       It runs n steps and in each step:
       - computes the directional variance in the point P
       - computes the gradient of the directional variance in P
       - moves one step 
           - of size: step_size 
           - from the point P 
           - along the direction of the gradient of the directional variance in P
       - repeats using the new point/direction as W
       At the end the function returns the direction of W    
    """
    guess = [ 1.0 for _ in data[0]]

    print(f"Start with guess: {guess} for {n} steps")
    with tqdm.trange(n) as t:
        print(f"T is {t}")
        for _ in t:
            dv = directional_variance(data, guess)
            gradient = directional_variance_gradient(data, guess)
            # new direction
            guess = gradient_step(guess, gradient, step_size)
            # we printout the directional variance
            # we rey to find the direction with greatest directional variance
            t.set_description(f"dv: {dv:.3f}")
    return direction(guess)        

# Now that we have the direction of the first principal component
# we can project the data against it
def project(v:Vector, w:Vector)-> Vector:
    """Projects v over w, returns a vector in the W direction
       The magintude is given by dot(v,w)
    """
    magnitude = dot(v,w)
    return scalar_multiply(magnitude,w)

# for further components analysis, we 
# remove the projction from teh data
# and repeat the steps
def remove_projection_from_vector(v: Vector, w:Vector)-> Vector:
    """subtract projection of v over w, from v"""
    return subtract(v, project(v,w))

def remove_projection(data:List[Vector], w:Vector) -> List[Vector]:
    """Remvoe the projection of v over w from every v in data"""
    return [ remove_projection_from_vector(v,w) for v in data ]

#
# Note this finds a predefined number of components
def pca(data: List[Vector], num_components: int) -> List[Vector]:
    """This finds a finite number of components: num_components for the data passed
       It returns a list of vector that are the directions of each component
    """
    components = []
    for _ in range(num_components):
        component = first_principal_component(data)
        components.append(component)
        data = remove_projection(data,component)
    return components
    

#
# Here we transfor the data based on the components found
def transform_vector(v: Vector, components:List[Vector]) -> List[Vector]:
    """This runs the projection of the vector v along the components
       returns a list of vectors (all the projections) 
    """
    return [ dot(v,w) for w in components ]

def transform(data:List[Vector], components: List[Vector]) -> List[Vector]:
    """For each v in data, this creates the projections along the components
       and return them all
       if we start we 10 data vectors and 2 components, the function will
       return 20 vectors note that they will be nested so
       it will actually return a list of 10 elements, each element is the list
       of vectors given by the projections
    """
    return [ transform_vector(v,components) for v in data ]

# Unfortunately there is no mention of the dataset used in the book.. so can't really test this here
# however it's maybe going to be used later in the book
# notes: scikit-learn implments all these methods