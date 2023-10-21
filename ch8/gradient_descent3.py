from gradient_descent2 import gradient_step
import random
from typing import Callable
import sys
sys.path.append("/home/vale6811/Desktop/oreilly/DSFS/ch4/")
from vector import Vector,vector_mean

#
# let's create a dataset of points with a linear relationship between them
actual_slope = 20
actual_intercept = 5
inputs =  [ (x, actual_slope * x + actual_intercept) for x in range(-50,50)]

#
# now we define a function that given a specific
# theta (slope, intercet)
# computes a y' prediction using a linear model based on x
# and returns the error y-y'
def linear_residual(x: float, y: float, theta: Vector) -> float:
    """
    This function fill get as parameter:
      x: <float> part of the dataset
      y: <float> part of the dataset and matches x, i.e. (x,y) is part of the dataset
      theta: <Vector> made of slope(float) and intercept(float) for a possible line

    The function will compute y' = intercept + slope * x
    and return y' - y
    """
    assert len(theta) == 2, "We only accept theta with 2 floats: slope and intercept"
    slope, intercept = theta
    predicted_y = intercept + slope * x
    return predicted_y - y

#
# the error function is given by ((( m*x ) + c ) - y )^2
# which can be rendered as ((( m*x ) + c )^2 +  y^2 - 2y * (( m*x ) + c )
#
# 1) Let's derive for m -> we get:
#      2x * (( m*x ) + c ) + 0 - 2y * x
#    this is also can be written collectin 2x as
#      2x * ((m*x + c) - y)
#    where ((m*x + c) - y) is the error so : 2x * error
# 2) Let's derive for c -> we get:
#      2 * (m*x + c ) * 1 + 0 - 2y * 1
#    this is also can be written collectin 2x as
#      2 * ((m*x + c) - y)
#    where ((m*x + c) - y) is the error so : 2 * error

def linear_gradient(x: float, y: float, theta: Vector) -> Vector:
    """
    This function fill get as parameter:
      x: <float> part of the dataset
      y: <float> part of the dataset and matches x, i.e. (x,y) is part of the dataset
      theta: <Vector> made of slope(float) and intercept(float) for a possible line

    The function will get the linear_residual and return the gradient (vector) as the vector
    of the partial derivates along the slope and the intercept

    """
    assert len(theta) == 2, "We only accept theta with 2 floats: slope and intercept"
    #
    residual_error = linear_residual(x,y,theta)
    #
    # the gradient on slope and intercept is given by this formula (see note above)
    # first one is the partial derivate for the slope
    # second one is the partial derivate for the intercept
    # in the point defined by residual error
    return [2 * residual_error * x, 2 * residual_error]


if __name__ == '__main__':
    #
    # intro
    print("We want to identify the slope of a set of paired values artifically created")
    print(f"The set is done by {len(inputs)} points in the following relationship between them")
    print(f"x, {actual_slope} * x + {actual_intercept}\n")
    #
    # random initial values for slope and intercept between -1 and 1
    theta_1 = [ random.uniform(-1,1), random.uniform(-50,50) ]
    theta_2 = theta_1.copy()
    theta_3 = theta_1.copy()
    print(f"Initial random theta (slope, intercept) is {theta_1}")
    #
    # learning rate
    learning_rate_1 = 0.0001
    learning_rate_2 = 0.001
    learning_rate_3 = 0.01
    print(f"Learning rate 1 is fixed: {learning_rate_1}")
    print(f"Learning rate 2 is fixed: {learning_rate_2}")
    print(f"Learning rate 3 is fixed: {learning_rate_3}")
    #
    # max_epoch = 20000
    max_epoch = 20000
    print(f"Starting model fit, max epoch is: {max_epoch} ")
    for epoch in range(max_epoch):
        #
        # we get the gradient for all the points in the dataset
        # grad_vector is a list of vectors [ (m1,c1), (m2,c2), .. ]
        grad_vector_1 = [ linear_gradient(x,y,theta_1) for (x,y) in inputs ]
        grad_vector_2 = [ linear_gradient(x,y,theta_2) for (x,y) in inputs ]
        grad_vector_3 = [ linear_gradient(x,y,theta_3) for (x,y) in inputs ]
        #
        # this gives as the mean slope and the mean intercept
        grad_vector_mean_1 = vector_mean(grad_vector_1)
        grad_vector_mean_2 = vector_mean(grad_vector_2)
        grad_vector_mean_3 = vector_mean(grad_vector_3)
        #
        # now we take a step using learning_rate in the direction (opposite) of the gradient
        theta_1 = gradient_step(theta_1, grad_vector_mean_1, -learning_rate_1)
        theta_2 = gradient_step(theta_2, grad_vector_mean_2, -learning_rate_2)
        theta_3 = gradient_step(theta_3, grad_vector_mean_3, -learning_rate_3)
        if epoch % 500 == 0: print(f"epoch {epoch} -  theta_1,2,3: {theta_1} - {theta_2} - {theta_3} ")


    print("Playing around with learning rate and initial theta I can see that")
    print("If the learning rate is too high, the system breaks and it misses the paramters")
    print("if the initial theta range is bigger it takes more epoch to coverge")
    print("if the learning rate is too little it might not get to teh result")



