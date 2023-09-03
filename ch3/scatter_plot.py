from collections import Counter
from matplotlib import pyplot as plt


friends = [ 70,  65,  72,  63,  71,  64,  60,  64,  67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
minutes_10 = [ x*10 for x in minutes]
labels =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

# label each point
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
        xy=(friend_count, minute_count), # Put the label with its point
        xytext=(5,0),                  # but slightly offset
        textcoords='offset points')

plt.title("Daily Minutes vs. Number of Friends")
plt.xlabel("# of friends")
plt.ylabel("daily minutes spent on the site")
# if x and y are similar ranges you might want to force the plot
# to use the same values in the axis (uncomment below)
# plt.axis("equal")


fig1 = plt.gcf()
plt.show()

fig1.savefig('ch3/scatter_plot.png')
#plt.gca().clear()
