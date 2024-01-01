#!/usr/bin/env python
import sys
from collections import Counter,defaultdict
from typing import List, NamedTuple, Dict
import os
import csv
current_path = os.path.abspath(".")
sys.path.append(f"{current_path}/ch4/")
from vector import Vector,distance

def raw_majority_vote(labels: List[str]) -> str:
    """Given a List of N strings (with duplicates) that represents
       the labels of the N nearest neighbours; this function will return
       the most common label

       Note: in case of a tie, the first label met among the ones with the
       highest count is returned
       e.g.
       'a','b','a','c' -> returns 'a'
       'a','b','a','b','c' -> returns 'a'
       'b','a','b','a','c' -> returns 'b'
    """
    votes = Counter(labels)
    # most_common(n) returns a list withthe n most common items
    # in a tuple where each item is mapped to the # of occurences
    # e.g. [ ('a','2'), ('b',2'), ()'c',1) ]
    # we take only the label of the first element
    winner,_ = votes.most_common(1)[0]
    return winner

assert raw_majority_vote(['a','b','c','a']) == 'a'
assert raw_majority_vote(['a','b','c','b']) == 'b'
assert raw_majority_vote(['a','b','a','b']) == 'a'

# If we have a tie we take care of it here
# Options are:
# - pick a winner at random
# - weight the votes by distance
# - reduce K until we find a unique winner
# Here we do the last option


def majority_vote(labels: List[str], debug:bool=False) -> str:
    """This function is similar to the previous one
       but:
       - it assumes that labels are ordered from nearestto farthest
         i.e. the first entry in the list is the one of the closest neighbour
       - if there is a tie it will
          - remove one neighbour from the dataset (the more dstant one)
          - call itself recursively
    """
    vote_counts = Counter(labels)
    if debug:
        print(f"labels list: {labels}")
    # this time we get both the winner and the # of votes
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len([count for count in vote_counts.values()
                       if count == winner_count]
                      )
    if debug:
        print(f"num winners: {num_winners}")
    if num_winners == 1:
        return winner
    #
    # else recursion with smaller dataset
    return majority_vote(labels[:-1])

#
# note that case 3 would have returned 'a' in previous function
assert majority_vote(['a','b','c','a']) == 'a'
assert majority_vote(['a','b','c','a','b']) == 'a'
assert majority_vote(['a','b','b','a']) == 'b'

#
# Now we create a classifier
#
# first define a Tuple with a label and a point from dataset
class LabeledPoint(NamedTuple):
    label: str
    point: Vector


def knn_classify(k: int, labeled_points: List[LabeledPoint],
                 new_point: Vector) -> str:
    """This function gets as input
       k: <int> the number of neighbours to consider
       labeled_points: <List[LabeledPoint]> the list ofLabeled points we have
       new_point: <Vector> a new point without Label

       The function will return the label for the new point
    """
    #
    # let's sort the point by distance to the new point    
    sorted_points = sorted(labeled_points, 
                           key=lambda p: distance(new_point,p.point) ) 
    #
    # find the labels of the nearest points
    # and return the most common
    k_nearest_labels = [ p.label for p in sorted_points[:k]]
    return majority_vote(k_nearest_labels)
#
#########################################################
#    PART TWO
#########################################################
#
# The next part requires a dataset setup
# The file is now available in the data_sets folder 
# the following (now commented) were used to download the file
# import requests
# data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
# with open("data_files/iris.dat","w") as f:
#    f.write(data.text)
#
# data is in csv format; columns are
# sepal_length, sepal_width, petal_length, petal_width, class
# the datset however has no headers
# e.g 5.0,3.6,1.4,0.2,Iris-setosa
 
def parse_iris_row(row: List[str]) -> LabeledPoint:
    """ this function gets as input a list of string from the iris dataset
        and returns an object of the named Typle Class Labeled Point
        the last element of the list is assigned to the label while
        the previous values create the data point vector
        e.g
        5.0,3.6,1.4,0.2,Iris-setosa
        label = setosa (other options are versicolor and virginica)
        vector = [5.0,3.6,1.4,0.2]
    """
    measures = [ float(x) for x in row[:-1]]
    label = row[-1].split("-")[-1]
    #
    return LabeledPoint(label,measures)


with open("data_files/iris.dat","r") as f:
    reader = csv.reader(f)
    # we create a list of Labeled Points
    # we also skip empty lines
    iris_data = [ parse_iris_row(row) for row in reader if row ]

#
# this is to order the points by species
points_by_species: Dict[str, List[Vector]] = defaultdict(list)
for iris in iris_data:
    points_by_species[iris.label].append(iris.point) 
    

# run the next part only if we call the file directly
if __name__ == '__main__':    
    #
    # The data points describe a 4 dimensional space so it is difficult to plot them
    # all in the same graph
    # we can however graph the pairs which in this case are (n*(n-1))/2 = (4*3)/2 = 6
    from matplotlib import pyplot as plt
    metrics = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    # this creates the 6 pairs combinatinos (1,2),(1,3),(1,4),(2,3),(2,4),(3,4)
    pairs_combinations = [ (i,j) for i in range(4) for j in range(4) if i < j ] 
    # we have 3 possible labels: setosa,virginica,versicolor so we use 3 
    # makers
    marks = [ '+', '.', 'x' ]
    #
    # now we create the graph (with 6 subplots: 2 rows x 3 columns)
    fig, ax = plt.subplots(2,3)
    fig.set_figheight(9)
    fig.set_figwidth(12)
    for row in range(2):
        for column in range(3):
            # this just return one of the possible combinations
            i,j = pairs_combinations[ (row*3) + column ]
            ax[row][column].set_title(f"{metrics[i]} vs {metrics[j]}", fontsize=8)
            ax[row][column].set_xticks([])
            ax[row][column].set_yticks([])
            #
            # we have 3 species (dict keys) and 3 markers so we zip them together
            # the result is (mark, species, list of points)
            for mark, (species, points) in zip(marks,points_by_species.items()):
                # here we create x and y values for each species (note species is singular..)
                xs = [ p[i] for p in points ]
                ys = [ p[j] for p in points ]
                ax[row][column].scatter(xs,ys, marker=mark, label=species)
    
    plt.show()
    