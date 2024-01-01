# CH12 NOTES  K NEAREST NEIGHBOUR

It requires:
- a notion of distance between points in the dataset
- the assumption that points that are close to one another are similar

It basically tries to make a prediction based on the value of the points in the training dataset; if the majority of "close" points are of one type (label), the new point is also classified as such type (label)

Becasue datapoints are usually vectors we can use Eucldean distance<p>
**Note:**   If we have a tie we can
 - pick a winner at random
 - weight the votes by distance
 - reduce K until we find a unique winner

&nbsp;  
&nbsp;
&nbsp;
The file: 
 - knearest1.py will 
    - implement the basic functions (including the classifier)
    - load the dataset
    - plot the iris datase
 - knearest2.py will split the dataset into training and test and run the classifier

&nbsp;
**Note:**  
ML DATASETS are available here: https://archive.ics.uci.edu

