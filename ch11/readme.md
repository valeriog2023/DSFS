# CH11 NOTES
The basic approach of Machine learning is to create a model based on existing data that
can be generalized to new data.
<p>
The best approach is to split the data into training set and verification set
The ration between the two is kind of arbitrary e.g.
*2/3* training and *1/3* verification or 
*80%/20%* training/verification etc..

<p>
Generically speaking once the data is split you would do something like:

```
model = someModel()
model.train(train_x,train_y)
performance = model.test(test_x,test_y)
```

However:
- there might be pattern in traiing and test set that do not generalize outside the existing data sets
- you can't use the same set to choose between different models
- if you have to compare models you should use 3 sets:
  - training set to build the model
  - a vlidation set set for choosing among the trained models
  - a test set to judge the final model 

## Catgorization problems performance
In catgorization problems you have 3 measures:
- **accurancy**: not overall a good measure, this is the ration between
             the cases identified correctly by the model and the 
             overall cases (see notes in ml1.py as why this is not 
             always meaningful)
    <p>
however the next 2 are better:             
- **precision**: this is the ration between the correctly ientified positive
             and all the possitives identified by the system
             **tp / (tp + fp)** 
- **recall**: this is the ration between the correctly identified positives
          and the actual positives: **tp / (tp + fn)**

**recall and precision** can be combined in a parameter called **f1_score** which is the harmonic mean of the two

**Note: precision and recall are a tradeoff..**
you can build a model that has zero flase negatives for instance (if it always guess positive) but it will have a high number of false postives
and viceversa



## BIAS vs VARIANCE
are ways to describe how the model would behave if it was trained
against different datasets from the same population.

**BIAS** is a systematic error (typically correspond to underfitting or
using a model that does not describe the reality).
E.G. using a linear model for a system with non linear relationships would imply a high bias.
In this case, training against different datasets would have a  high
error rate and fail to capture the actual trend.
The resulting models would however look similar (low variance)

**VARIANCE** is how much the model would change based on the actual dataset
used for training. this is generally associated with overfitting or
too compelx models
