#
# A scatter plot is useful for 2 dimensions datasets but for N dataset we can see correlation
# as a matrix where the cell i,j gives the correlation between dataset i and dataset j
# Of course we have that:
#  - the matrix is symmetric: correlation(i,j) == correlation(j,i)
#  - main diagonal has all ones: correlation(i,i) == 1
from typing import List, Dict
import matplotlib.pyplot as plt
import sys
sys.path.append("ch6/")
sys.path.append("ch4/")
sys.path.append("ch5/")
from probability3 import inverse_normal_cdf
from statistics3 import correlation
from data2 import random_normal
#
# note as a reminder Matrix is a List[List[float]]
# note as a reminder Vector is a List[float]
# note as a reminder make_matrix gets as input row, columns and 
# a function that s called to fill in the matrix
from matrices import Matrix,Vector,make_matrix

def correlation_matrix(data:List[Vector])-> Matrix:
    """
    This function will get as in input a list of dataset of same length
    and then it will compute the correlation between each pairs and
    return a matrix that stores the correlation values..
    Note, of course that:
     - the matrix is a sqaure matrix with size: len(data)
     - the matrix is symmetric: correlation(i,j) == correlation(j,i)
     - main diagonal has all ones: correlation(i,i) == 1    
    """
    #
    # we define an internal function that we then pass to make_matrix
    # data[i] and data[j] are both lists
    def correlation_ij(i:int,j:int) -> float:
        """returns the correlation between datasets in position i and j"""
        return correlation(data[i], data[j])
    #
    # now we make a matrix (passing the function created)
    return make_matrix(len(data),len(data),correlation_ij)

print("Regenerating 3 vectors and..")
xs = [ random_normal() for _ in range(1000)]
ys1 = [  x + random_normal() / 2 for x in xs]
ys2 = [ -x + random_normal() / 2 for x in xs]
print("Checking that the matrix has been created correctly")
vectors = [xs, ys1, ys2]
assert correlation_matrix(vectors) == [
    [correlation(xs,  xs), correlation(xs,  ys1), correlation(xs,  ys2)],
    [correlation(ys1, xs), correlation(ys1, ys1), correlation(ys1, ys2)],
    [correlation(ys2, xs), correlation(ys2, ys1), correlation(ys2, ys2)],
]

if __name__ == "__main__":
    #
    # we just subplot all the correlations
    # in a n x n subplot matching the correlation matrix
    num_vectors = len(vectors)
    fig,ax = plt.subplots(num_vectors,num_vectors)
    #
    #
    for i in range(num_vectors):
        for j in range(num_vectors):
            #
            # scatter plot diagram of i,j
            # Scatter column_j on the x-axis vs column_i on the y-axis,
            if i != j: ax[i][j].scatter(vectors[j], vectors[i])
            # 
            # unless i == j, in which case show the series name.
            # annotate, makes a note on a point
            else: ax[i][j].annotate("series " + str(i),       # what to write 
                                    (0.5, 0.5),               # point to annotate
                                    xycoords='axes fraction', #coordinate system the point is given in
                                    ha="center", va="center") # this move the string to the center?
            #
            # Then hide axis labels except left and bottom charts
            if i < num_vectors - 1: ax[i][j].xaxis.set_visible(False)
            if j > 0: ax[i][j].yaxis.set_visible(False)            
    #
    # Fix bottom right and top left axis labels
    # because we write the name of the series, the numbers in the legend would be different
    # so we reset them. we don't care about the ons inside as we don't actually show them
    ##
    # Last subplot, set the xlimit as the same as plot on the first row last column
    ax[-1][-1].set_xlim(ax[0][-1].get_xlim())
    # first subplot, set the ylimit as the same as plot on the first row second column
    ax[0][0].set_ylim(ax[0][1].get_ylim())    
    plt.show()        