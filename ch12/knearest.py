#!/usr/bin/env python
import sys
from collections import Counter
from typing import List, NamedTuple

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