import random
from typing import TypeVar, List, Tuple

################################
#  SPLIT THE DATA
################################

x = TypeVar('X') # generic type to represent an input data point
y = TypeVar('Y') # generic type to represent an output data point

def split_data(data: List[x], prob: float) -> Tuple[ List[x], List[x] ]:
    """
    This method will split the initial dataset into 2 randomly generated
    sets based on the probability given: [prob, 1-prob]
    """
    copied_data = data[:]
    random.shuffle(copied_data)
    cutoff = int(len(data) * prob)
    return (copied_data[:cutoff],copied_data[cutoff:])

# let's generate 1000 points
# and split them based on probability 0.75
data = [ n for n in range(1000) ]
p = 0.75
train,test = split_data(data,p)

#
# let's verify some basic checks
assert len(train)==750
assert len(test)==250
assert data == [ n for n in range(1000) ]  # original data did not change
assert sorted( train + test) == data       # new data is the same when sorted
#
#
def train_test_split(xs: List[x],
                     ys: List[x],
                     test_pct: float ) -> Tuple[ List[x], List[x],
                                                 List[y], List[y]]:
    """This function is basically the same as before but instead of splitting
       only the input data set, it also split the result of some model (ys)
       into a training and test set
    """
    #
    # to slit xs and ys and keep them matched, we generate a lsit of
    # index, spilt the index split and assign elements xs,ys based on where
    # their index ends up
    idxs = [i for i in range(len(xs))]
    train_idxs, test_idxs = split_data(idxs,(1-test_pct))

    return ([ xs[i] for i in train_idxs ],
            [ xs[i] for i in test_idxs ],
            [ ys[i] for i in train_idxs ],
            [ ys[i] for i in test_idxs ]
            )

#
# Again let's run some basic assert
xs = [x for x in range(1000) ] # note we don't assign a rang because it would nt be type list
ys = [2*x for x in xs ]
test_pct = 0.25  # let's split the test in 3 to 1 ration
train_x, test_x, train_y, test_y = train_test_split(xs,ys,test_pct)
assert len(train_x) == len(train_y) == 750
assert len(test_x) == len(test_y) == 250
# we want to verify that the split is correct
assert all( y == 2 * x for x,y in zip(train_x,train_y) ), f"Error for x: {x} , y: {y}"
assert all( y == 2 * x for x,y in zip(test_x,test_y) ), f"Error for x: {x} , y: {y}"
#
# Generaically speaking now that the data is split you would do something like
#model = someModel()
#model.train(train_x,train_y)
#performance = model.test(test_x,test_y)
#
#
################################
#  PERFORMANCE EVALUATION
################################
# Assuming we are talking about classification
# or a binary result, we can have
# - true positive
# - false positive
# - true negatives
# - false negatives
#
######## ACCURACY
# is defined as the fraction of correct predictions

def accuracy(tp: int, fp: int, fn: int, tn: int) -> float:
    """
    Given
    # - tp: true positive
    # - fp: false positive
    # - fn: false negatives
    # - tp: true negatives
    it will return: correct / total : (tp +tn)/(tp +tn +fn +fp)

    """
    return (tp + tn) / (tp +fp + tn + fn )
#
# note the values are taken from an example in the book
# where wh use the name "luke" as a test for Leukemia and
# we have
# - 1,000,000 people               -> the test will give 981070 true negatives**
# - 5000 Luke                      -> the test will give 4930 false positives
# - 70 Luke with Lukemia           -> the test will get a true positive
# - 14,000 people with Leukemia    -> the test will give 13930 false negatives
# Note **: 981070 comes up because
#          - the test identifies 5000 positives and 995000 negatives (all people not called Luke)
#          - there are instead 14000 positives and 70 are identified correctly so 13930 are not identified
#            correctly and are left inside the 995000 negatives
# so the actual true negatives are 995,000 - 13,930 = 981,070
#
## NOTE:  ACCURANCY IS PRETTY HIGH EVEN IF THE TEST IS S**T
## THAT'S BECAUSE OF THE HIGH NUMBER OF TRUE NEGATIVES
assert accuracy(70,4930,13930,981070) == 0.98114
#
#
######## PRECISION
# How accurate are positive results
def precision(tp: int, fp: int, fn: int, tn: int) -> float:
    """
    Given
    # - tp: true positive
    # - fp: false positive
    # - fn: false negatives
    # - tp: true negatives
    it will return: tp / (tp + fp )

    Precision is the ratio between the correctly identified positives 
    and all the positives identified by the model
    """
    return tp  / (tp +fp )

## NOTE: PRECISION IS VERY LOW
## in this case it's 70 over 5000
assert precision(70,4930,13930,981070) == 0.014

######## RECALL
# How many of the positive results we identified overall
def recall(tp: int, fp: int, fn: int, tn: int) -> float:
    """
    Given
    # - tp: true positive
    # - fp: false positive
    # - fn: false negatives
    # - tp: true negatives

    it will return: tp / (tp + fn )
    Recall is the ratio between the correctly identified positives 
    and all the actual positives 
    """
    return tp  / (tp +fn )

## NOTE: RECALL IS ALSO VERY BAD
## in this case it's 70 over 14000
assert recall(70,4930,13930,981070) == 0.005


########  F1 SCORE = PRECISION + RECALL
def f1_score(tp: int, fp: int, fn: int, tn: int) -> float:
    """Combines precision and reall into a single value
       using the formula =  2 * precision * recall / (precision + recall)
       
       Note: this is also the harmoni mean of the 2 values
       H(x1,x2,..,xn ) = n / (1/x1 + 1/x2 + ... + 1/xn)
       and for 2 values
       2 / (x1 + x2 / x1*x2 ) = 2*(x1*x2) / (X1 + x2)
    """
    p = precision(tp,fp,fn,tn)
    r = recall(tp,fp,fn,tn)

    return 2 * p * r / ( p + r)