from typing import List, Dict
import random
import matplotlib.pyplot as plt
import sys
sys.path.append("ch6/")
sys.path.append("ch5/")
from probability3 import inverse_normal_cdf
from statistics3 import correlation
from data1 import plot_histogram

def random_normal()-> float:
    """returns a random draw from a standard normal distribution"""
    return inverse_normal_cdf(random.random())

if __name__ == "__main__":
    # this gives 1000 points randomly picked from a random normal distribution
    xs = [ random_normal() for _ in range(1000)]
    # this gets another draw of 1000 points and shifts it up of the previous value divided by 2
    ys1 = [  x + random_normal() / 2 for x in xs]
    # this gets another draw of 1000 points, inverts the sign and shifts it up of the previous value (xs) divided by2
    ys2 = [ -x + random_normal() / 2 for x in xs]
    
    # to plot them as histogram I scale the values up *100
    plot_histogram([ x*100 for x in xs ],bucket_size=10,title="standard normal distribution")
    plot_histogram([ x*100 for x in ys1],bucket_size=10,title="standard normal distribution shifted up")
    plot_histogram([ x*100 for x in ys2],bucket_size=10,title="standard normal distribution inverted and shifted up")
    print("They all look very similar but..")
    plt.scatter(xs,ys1,marker='.',color='black',label='ys1')
    plt.scatter(xs,ys2,marker='.',color='red',label='ys2')
    plt.xlabel("xs")
    plt.ylabel("ys")
    plt.title("ys1 vs ys2 Distributions")
    plt.legend(loc='best')
    plt.show()
    print(f"Correlation of xs and ys1 is: {correlation(xs,ys1)}")
    print(f"Correlation of xs and ys2 is: {correlation(xs,ys2)}")
    print(f"Correlation of ys1 and ys2 is: {correlation(ys1,ys2)}")
