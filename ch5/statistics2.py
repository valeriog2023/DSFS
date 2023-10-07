from collections import Counter
# every entry is the number of friends a person has
# there are 204 values
# max value is 100 (present 1 time)
# min value is 1 (present 22 times)
num_friends = [100,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]


def mean(v:list[float])->float:
    """Returns the arithmetic mean from a vector of floats
       e.g. v: [3,4,5]
       returns (3+4+5)/3 = 4
    """
    return sum(v)/len(v)

def median(v1:list[float])->float:
    """Returns the middle value of the list if the list contains an odd number of elements
       Returns the mean of the two niddle values if the the list contains an even number of elements
       E.G.
       median([3,6,8])    -> 6
       median([3,6,8,10]) -> 7 (as in (6+8)/2)
       Note: the median will require to sort the values in the list
    """
    v = sorted(v1)
    assert len(v) > 0, "The list needs to contain at least one element"
    if len(v) == 1:
        return v[0] 
    elif len(v) % 2 == 1:
        return v[ len(v) // 2 ]  # the // returns the lower integer that come from the normal division operation 
    else:
        high_midpoint = len(v) //2
        return mean([ v[high_midpoint-1], v[high_midpoint] ] )


def quantile(xs: list[float], p: float) -> float:
    """Returns the value in xs at the pth-percentile"""
    assert p <= 1, "p must be between 0 and 1"
    assert p >=0, "p must be between 0 and 1"    
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]

assert quantile(num_friends, 0.10) == 1
assert quantile(num_friends, 0.25) == 3
assert quantile(num_friends, 0.75) == 9
assert quantile(num_friends, 0.90) == 13


def mode(xs:list[float]) -> list[float]:
    """Returns a list (there can be more than one mode)
       of the most common values in the input list
       E.G.
       mode([1,1,1,3,2,5,4,3,2,1,2,2]) == [1,2]
    """
    c = Counter(xs)
    # get me the 1st most common value (there might be other with the same value)
    # actually ignore the value and only keep the count
    _, most_common_value = c.most_common(1)[0]
    #
    # now return the list of values that have their counter equal to most_common_value
    return [ value for value,frequency in c.items() if frequency == most_common_value ]

assert mode([1,1,1,3,2,5,4,3,2,1,2,2]) == [1,2]


print(f"The mean of our data points is {mean(num_friends)}")
print(f"The median of our data points is {median(num_friends)}")
print(f"The value at the 15% (0.10) percentile is {quantile(num_friends,0.1)}")
print(f"The value at the 15% (0.25) percentile is {quantile(num_friends,0.25)}")
print(f"The value at the 15% (0.75) percentile is {quantile(num_friends,0.75)}")
print(f"The value at the 15% (0.95) percentile is {quantile(num_friends,0.95)}")
print(f"The mode returned is: {mode(num_friends)}")