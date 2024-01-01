# CH12 - NOTES  ON NAIVE BAYES 

## Basic Idea

The idea is to use conditional probability to classify a datapoint.  
In particular:
&nbsp;
  
Let's assume (in a very simple model) that:  
**P(S)** is the probability a message is spam  
**P(B)** is the probability a message contains the word bitcoin

then we have:  
```
P(S & B) = P(S|B) * P(B) = P(B|S) * P(S), so:  
P(S|B) = [ P(B|S) * P(S) ] / P(B)  and by splitting P(B)  
P(S|B) = [ P(B|S) * P(S) ] / [ P(B|S)*P(S) + P(B|~S)*P(~ S) ]

                                         P(B|S) * P(S) 
Same as above..           P(S|B) = ----------------------------------
                                    P(B|S) * P(S)  +  P(B|~S) * P(~S) 

where ~ is used to represent the logical not condition
```

if we have a large collection of messages that we know are *spam* or *non spam*
we can easily find:

- **P(B|S)**  the probability of having the word bitcoin in a spam message 
- **P(B|~S)** the probability of not having the word bitcoin in a spam message 

For the probablity of a message being spam: **P(S)** (or not: **P(~S)**) we can
- either assume tha it's the same (this is what the book does.. a bit too naive maybe)
- use the proportion we get from our set of messages already classified (training set)

## A more sophisticated Spam Filter

Let's assume we have a vocabulary of words **W1, .., Wn**