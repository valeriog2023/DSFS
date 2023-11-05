import sys
sys.path.append("ch4/")
from vector import distance,vector_mean,Vector
sys.path.append("ch5/")
from statistics3 import standard_deviation
from typing import Tuple,List

###########################################################
# HERE WE SEE HOW DISTANCE CAN CHANGE BASED ON THE
# UNIT OF MEASURE VIA RESCALING
###########################################################
# Let's say we have a collection of weight and height in cm
# and we want to identify clusters
# we might need to use the concept of distance between points
# if one of the unit is converted (e.g to inches), the distance
# between the points will of course change
# A = [63,150]
# b = [67,160]
# c = [70,171]
print("Distances when using inches/pounds between data points # A = [63,150], B = [67,160], C = [70,171]")
a_to_b_distance = distance([63,150],[67,160])
a_to_c_distance = distance([63,150],[70,171])
b_to_c_distance = distance([67,160],[70,171])
print("a to b: ",a_to_b_distance )
print("a to c: ",a_to_c_distance )
print("b to c: ",b_to_c_distance )
print("Distances when using cm/pounds between same data pointsinches converted into cms")
a_to_b_distance = distance([160,150],[170.2,160])
a_to_c_distance = distance([160,150],[177.8,171])
b_to_c_distance = distance([170.2,160],[177.8,171])
print("a to b: ",a_to_b_distance )
print("a to c: ",a_to_c_distance )
print("b to c: ",b_to_c_distance )
#
print("""To get relationships it is difficult to compare data in different unit
so we normalize the data so that all dataset dimensions have std = 1 and mean = 0

This process is knowsn as RESCALING
      """)

#
#
def scale(data: List[Vector], sample:bool=False,verbose:bool=False)->Tuple[Vector,Vector]:
    """This method gets as input:

           data: A list of vectors, i.e. a list of lists[float]
           sample: a boolean, it affects the way the standard deviation is generated

       it will then compute the mean of each vector and the vector standard deviation
       It will then return a tuple with 2 elements:
         the first is the vector/list of means
         the second is the vector/list of standard deviation
    """
    dim = len(data[0])
    #
    # note that we get the values across the vectors
    # data = [ (v1,v2), (v3,v4),(v5,v6),..]
    # we create 2 vectors:
    #  first[ v1,v3,v5, ..]
    #  then [ v2,v4,v6, ..]
    # mean and standard deviations are for those
    means = vector_mean(data)
    if verbose:
        print(f"Data is: {data} with {dim} dimensions")
        print(f"Vector means are : {means}")
    stdevs = [ standard_deviation([vector[i] for vector in data ], sample=sample)
                for i in range(dim)
                ]

    return (means,stdevs)
#
# so each vector is a datapoint of dimension N
# in this example we have a symmetric matrix
# and it's ot really clear if he works on columns or rows
#  -3  -1  1  <- vector 1
#  -1   0  1  <- vector 2
#   1   1  1  <- vector 3
#   a   b  c  <- vector 4
# .....
# but the function vector mean and standard deviation works on columns!
# so we have 3 means and 3 std and the first one are taken across the vectors
# e.g. mean_1 is (-3 + -1 + 1 + a )/ 4
# that is a bit masked in the example because of the symmetricity of the matrix

vectors = [[-3,-1,1],[-1,0,1],[1,1,1]]
means,stdevs = scale(vectors,sample=True)
print("Given: vectors (as samples)= [[-3,-1,1],[-1,0,1],[1,1,1]]")
print(f"This gets:\nmeans={means}\nstdevs={stdevs}  # Note: if the vectors were population, the results would be different")
assert means == [-1,0,1]
assert stdevs == [2,1,0]
#
#
#
def rescale(data: List[Vector], verbose:bool=False)->List[Vector]:
    """
    This function will get as input

        data: A list of vectors, i.e. a list of lists[float]

    and it will find the standard deviation and mean of each vector (considerd as sample not population)
    return a list of vectors from the initial one where each data point is computed as:

        new_data_point = (old_data_point - vector_mean ) / vector_standard_deviation

    This means the resulting vector will have mean zero and standard deviation 1

    Note: one exception is if the standrd deviation is zero, in that case, the datapoints are left untouched
    """
    # get the means and dtd_devs
    dim = len(data[0])
    means,stdevs = scale(vectors,sample=True)
    if verbose:
        print(f"Data is: {data} with {dim} dimensions")
        print(f"Vector means and stds are are : {means} , {stdevs}")
    #
    # we start from a copy of the original vectors
    rescaled = [v[:] for v in data]

    for vector_index,v in enumerate(rescaled):
        #
        # for each dimension
        for i in range(dim):
            #
            # skip the vector if std dev == 0
            if stdevs[i] == 0:
                if verbose: print(f"Skipping dimension {i}.. standard deviation == 0")
                continue
            #
            if verbose:
                print(f"changing point {vector_index} of dimension {i}: ({v[i]}) to {(v[i] - means[i]) / stdevs[i]}")
            v[i] = (v[i] - means[i]) / stdevs[i]
    #
    return rescaled

rescaled_vectors = rescale(vectors)
print("-------------------\nAfter rescaling..")
print(f"Rescaled vectors are: {rescaled_vectors}")
means,stdevs = scale(rescaled_vectors,sample=True)
print(f"This gets:\nmeans={means}\nstdevs={stdevs}")