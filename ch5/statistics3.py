import math
from typing import List

def mean(xs: List[float]) -> float:
    """This function gets as input a List of float
       and returns a float which represents the mean value of the elements in the list
    """
    return sum(xs) / len(xs)

def de_mean(xs:List[float]) ->List[float]:
    """
    This function computes the mean of the input List xs
    and returns a List with the elemnts of xs - the mean of the xs list

    The result is a list of elements that have zero mean
    """
    xs_mean = mean(xs)
    return [x-xs_mean for x in xs]


def variance(xs: List[float], sample:bool=False, verbose:bool=False)-> float:
    """This function gets as input a List of float
       and returns a float which represents the standard deviation

       Note: that if we are using this method to get the standard deviation
             for a population, we divide the sum of squares by the number of elements
             if this is for a sample of the population, we divide by the sample length -1
             to get an unbiased measure
    """
    xs_mean = mean(xs)
    sample_std = sum([ (x-xs_mean)**2 for x in xs ]) / (len(xs) -1)
    population_std = sum([ (x-xs_mean)**2 for x in xs ]) / len(xs)
    if verbose:
        print(f"input is {xs}")
        print(f"mean is {xs_mean}")
        print(f"sample standard deviation is {sample_std}")
        print(f"population standard deviation is {population_std}")
    # Note: using here ** instead of ^ as the latter only supports int
    if sample:
        return sample_std
    else:
        return population_std


def standard_deviation(xs: List[float], sample:bool=False, verbose:bool=False) -> float:
    """This function gets as input a List of float
       and returns a float which represents the standard deviation

       Note: if we want the standard deviation for a sample we need to
             use sample: true, this will fix the variance and make the
             statistics unbiased
    """
    v = variance(xs, sample=sample, verbose=verbose)
    if verbose:
        print(f"input is {xs}")
        print(f"variance is: {v}")
    return math.sqrt(v)

test1 = [2,4,6]
test2 = [1,2,4,6,7]
test3 = [1,1,4,7,7]
print("testing")
print(f"Mean of {test1}: {mean(test1)}")
print(f"Mean of {test2}: {mean(test2)}")
print(f"Mean of {test3}: {mean(test3)}")
print(f"Variance of {test1}: {variance(test1)}")
print(f"Variance of {test2}: {variance(test2)}")
print(f"Variance of {test3}: {variance(test3)}")
print(f"STD of {test1}: {standard_deviation(test1)}")
print(f"STD of {test2}: {standard_deviation(test2)}")
print(f"STD of {test3}: {standard_deviation(test3)}")

def covariance(xs:List[float], ys:List[float]) -> float:
    """
    This function returns the co variance between two list of floats
    that have the same number of elements
    This is defiend as follows:
    xs = [x1,x2,x3], get the mean and subtract it from every element in xs
    ys = [y1,y2,y3], get the mean and subtract it from every element in ys

    Returns:    (xs_zero_mean dot_product ys_zero_mean) / N
    """
    assert len(xs) == len(ys), "the two lists have different size.. can't get covariance"
    xs_zero_mean = de_mean(xs)
    ys_zero_mean = de_mean(ys)

    return float(sum([xs_zero_mean[i] * ys_zero_mean[i] for i in range(len(xs)) ])) / len(xs)


def correlation(xs:List[float],ys:List[float]) -> float:
    """
    Returns a correlation for the input lists xs and ys
    The correlation value is between -1 and 1

    and it is defined as the covariance divided by the product of the standard deviations of the 2 lists
    Note: if one has std == 0 then the correlation is zero
    """
    xs_std = standard_deviation(xs)
    ys_std = standard_deviation(ys)
    if xs_std == 0 or ys_std == 0:
        return 0
    #
    return covariance(xs,ys) / (xs_std * ys_std)



print(f"covariance between test2 and test3 = {covariance(test2,test3)}")
print(f"Correlation between test2 and test3 = {correlation(test2,test3)}")