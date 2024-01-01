#!/usr/bin/env python
import sys
import os
current_path = os.path.abspath(".")
sys.path.append(f"{current_path}/ch11/")
from ml1 import split_data
from knearest1 import majority_vote, knn_classify
from knearest1 import iris_data, points_by_species # this is the data created
import random
from typing import Tuple,Dict
from collections import defaultdict

random.seed(12)
iris_train,iris_test = split_data(iris_data, 0.70)

assert len(iris_train) == 0.7 * len(iris_data)
assert len(iris_test) == 0.3 * len(iris_data)

# Here we need to choose K and run the classifier
# Note that if we chose a K too big we are just going
# to classify everything as the most common element
# if k is too small we are too sensitive to outliers
# In a real case scenario we might have a third set
# used to choose k before running the validation/test set

# this is a dictionary that will use 
# as key: a tuple with 2 labels: predicted, actual 
#         (this is the event where we predicted one label vs actual label)
# as value: an integer that keeps count of how many times the even occurred
confusion_matrix: Dict[Tuple[str,str], int] = defaultdict(int)
num_correct = 0
k=5

for iris in iris_test:
    predicted = knn_classify(k, iris_train, iris.point)
    actual = iris.label

    if predicted == actual:
        num_correct += 1
    # we also update the matrix of results
    confusion_matrix[(predicted,actual)] += 1    

pct_correct = num_correct / len(iris_test)
print(f"Using {k} neighbours, we correctly predicted {pct_correct} points in the test dataset")        
print("Full results here:")
for pair,value in confusion_matrix.items():
    print(f"Pair (predicted/actual): {str(pair):30} : {value}")