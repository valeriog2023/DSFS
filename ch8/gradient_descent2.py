from gradient_descent1 import estimate_gradient
import random
from typing import Callable
import sys
sys.path.append("/home/vale6811/Desktop/oreilly/DSFS/ch4/")
from vector import Vector,distance,scalar_multiply,add

msg = """
#
# Here we test the gradient descent against the sum of sqaure function
# Note that the sum of square function has an absolute minumum when
# each element of v is zero
"""
print(msg)


def gradient_step(v: Vector, gradient: Vector, step_size: float) -> Vector:
    """
    This function taks as in input:
       v: coordinate of a point in the space
       gradient: vector of partial derivates of a function f (must be in the same dimension of v)
       ste_size: size of the step to take from v in the gradient direction

    it returns the coordinates of the point reached starting from v and moving step_size in the
    gradient direction
    """
    #
    # basic check
    assert len(v) == len(gradient), f"initial point and gradient vectors must be of the size got instead v ({len(v)}, gradient ({len(gradient)})"
    #
    # return the new point
    return add(v, scalar_multiply(step_size,gradient) )


print("running basic gradient step assert")
assert gradient_step([1,1,1], [1,1,1], 1) == [2,2,2]
assert gradient_step([1,1,1], [1,0,1], 1) == [2,1,2]
assert gradient_step([1,1,0], [1,0,1], 2) == [3,1,2]
print("running basic gradient step assert - done")

def sum_of_square_gradient(v: Vector) -> Vector:
    """This function gets a Vector as in input and returns
       The vector of the partial derivates for the function sum of squares
       f(v) := sum [ (xi ^ 2) for xi in v ]
       when we do the gradient of partial derivates, all terms are constant
       except the i ew are considering so the
       resulting gradient vector is [ 2*xi for xi in v ]
    """
    return [ 2*x for x in v]


if __name__ == '__main__':
    #
    # create a random vector size 3
    # the uniform function returns a random number between 2 values
    # 2 extremes included
    print("Test 1. create a random vector in R3 wih components between -10 and 10")
    print("Using the gradient of sum of squares function we reach the min of the function (0,0,0) ")
    initial_v = [ random.uniform(-10,10) for i in range(3) ]
    v = initial_v.copy()
    #
    # set a tolerance
    tolerance = 0.0001
    #
    # walk the function
    for epoch in range(1000):
        # get the gradient in v
        grad = sum_of_square_gradient(v)
        # take a negative step in grad direction and recompute v
        v = gradient_step(v, grad, -0.01)
        print(epoch, v)
        #
        # stop if we are close enough
        if distance(v, [0,0,0]) < tolerance: break


    assert distance(v, [0,0,0]) < tolerance, f"the final distance after 1000 iterations should be zero with tolerance {tolerance} but it's {distance(v, [0,0,0])}"
    print(f"got from {initial_v} close to [0,0,0] with tolerance {tolerance} and a step of -0.01 in {epoch} iterations")

