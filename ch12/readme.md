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
 - kneares3.py will run some test to show the **"curse of Dimensionality"**
   In a lowest dimension space, the closest points tend to be much closer than
   than the average distance (so the process of checking the neighbours makes sense)
   However as the number of dimensions grow, the distance tends to get close to the
   average so the method does not mean much anymore
   Another way to think about that is the density of the sample in the space; as the
   number of dimensions grow, the density gets lower.
   

&nbsp;
**Note:**  
ML DATASETS are available here: https://archive.ics.uci.edu

