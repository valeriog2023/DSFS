from gradient_descent2 import gradient_step
from gradient_descent3 import linear_gradient
import random
from typing import Callable,TypeVar,Iterator,List
import sys
sys.path.append("/home/vale6811/Desktop/oreilly/DSFS/ch4/")
from vector import vector_mean
#
# This allows us to type "generic" functions
T = TypeVar('T')
#
# let's create a dataset of points with a linear relationship between them
actual_slope = 20
actual_intercept = 15
inputs =  [ (x, actual_slope * x + actual_intercept) for x in range(-50,50)]
#
#
# instead of computing the gradient for all the elemnts in the dataset
# we can run the computation on a subset of the dataset. This is called
# minibatch
# we crate a function that:
#  - returns an iterator over a subset of the generic dataset
#  - the subset has size batch_size or smaller
#      - the dataset is split into smaller sequential chunks of size batch_size
#        the last batch can be smaller if batch_size does not divide the dataset perfetcly
#      - the possible batches from the dataset can be shuffled
#      - the function returns the different batches possibly shuffled
def minibatches(dataset: List[T],   # dataset is a list of a type generic T; what ever this type is
                                    # the function will return an iterator that gives list of the
                                    # same type
                batch_size: int,
                shuffle: bool = True
                ) -> Iterator[List[T]]:  # this is what is returned: an iterator that for every
                                         # cycle gives a list of type T matching the type of the
                                         # initial dataset list
    """
    This method takes as input:
     - dataset: a lsit of a specific type: str,int,etc..
     - batch_size: an int that should be smaller than the list length
     - shuffle: boolean if set to true the resulting batches are going to be shuffled
                default: true

    and it returns an iterator that gives a list of size batch_size from the dataset
    (the batch can be smaller if batch_size does not divide dataset perfectly)
    e.g.
    len(dataset) = 80
    batch_size = 25
    shuffle = False
    the iterator will give:
     dataset[0:24]
     dataset[25:49]
     dataset[50:74]
     dataset[75:]
    if shffle is True, the order of the dataset returned is random (the elements are still
    sequentially assigned to each batch)
    """
    batch_starts = [ start for start in range(0,len(dataset),batch_size) ]
    #
    # randomize
    if shuffle: random.shuffle(batch_starts)
    #
    #
    for start in batch_starts:
        end = start + batch_size
        ## if end is > len(dataset) it will just return what is available
        yield dataset[start: end]



if __name__ == "__main__":
        #
    # random initial values for slope and intercept between -1 and 1
    theta = [ random.uniform(-1,1), random.uniform(-1,1) ]
    theta_batches_1 = theta.copy()
    theta_batches_2 = theta.copy()
    theta_batches_3 = theta.copy()
    batch_size_1 = 10
    batch_size_2 = 20
    batch_size_3 = 40
    #
    # learning rate
    learning_rate = 0.0001
    print(f"Learning rate is fixed: {learning_rate}")
  #
    # max_epoch = 5000
    max_epoch = 1000
    print(f"Starting model fit, max epoch is: {max_epoch} ")
    for epoch in range(max_epoch):
        #
        # we get the gradient for all the points in the dataset
        # grad_vector is a list of vectors [ (m1,c1), (m2,c2), .. ]
        # Normal gradient vector/mean
        grad_vector = [ linear_gradient(x,y,theta) for (x,y) in inputs ]
        grad_vector_mean = vector_mean(grad_vector)
        theta = gradient_step(theta, grad_vector_mean, -learning_rate)
        #
        #
        # same as above but for the batches
        # the different is that splitting the computation in batches
        # makes it more efficient
        # it also converges much quicker
        for batch in minibatches(inputs,batch_size_1,True):
            grad_vector_batch = [ linear_gradient(x,y,theta_batches_1) for (x,y) in batch ]
            grad_vector_batch_1_mean = vector_mean(grad_vector_batch)
            theta_batches_1 = gradient_step(theta_batches_1, grad_vector_batch_1_mean, -learning_rate)
        #
        # batch 2
        for batch in minibatches(inputs,batch_size_2,True):
            grad_vector_batch = [ linear_gradient(x,y,theta_batches_2) for (x,y) in batch ]
            grad_vector_batch_2_mean = vector_mean(grad_vector_batch)
            theta_batches_2 = gradient_step(theta_batches_2, grad_vector_batch_2_mean, -learning_rate)
        #
        # batch 3
        for batch in minibatches(inputs,batch_size_3,True):
            grad_vector_batch = [ linear_gradient(x,y,theta_batches_3) for (x,y) in batch ]
            grad_vector_batch_3_mean = vector_mean(grad_vector_batch)
            theta_batches_3 = gradient_step(theta_batches_3, grad_vector_batch_3_mean, -learning_rate)


        #
        # this gives as the mean slope and the mean intercept
        if epoch % 100 == 0:
            #print(f"-------------- epoch {epoch}")
            print(f"{epoch:3}: full {theta} - batch({batch_size_1}) theta {theta_batches_1} batch({batch_size_2}) theta {theta_batches_2} b({batch_size_3}) theta {theta_batches_3}")
    #
    print(f"Learning rate: {learning_rate}")
    print(f"Actual slope/intercept: {actual_slope}/{actual_intercept}\nAs you an see the batch method converges quicker..")

    print("-----")
    print("Notes:\n - when you compute the gradeint descent for the whole dataset is some time still called: batch gradient descent ")
    print(" - stochatstic gradient descent can be used to refer to the method with batches or when you actually move")
    print("   one step for each point")
    print("In our case, batches optimizes the search and in this very specific case taking the gradient for every time")
    print("will get quicker result but it's not always the case")